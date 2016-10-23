from django.http import HttpResponse
import datetime
import json
from api.models import Client, Event, Coc
from django.http import HttpResponseRedirect
import collections
from decimal import Decimal
from django.forms.models import model_to_dict
from django.db.models import F
from dateutil import parser
from django.db.models import Q
from django.contrib.auth import logout
from custom_decorators import print_errors

def json_custom_parser(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    elif not isinstance(obj, basestring) and isinstance(obj, collections.Iterable):
        return list(obj)
    elif isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19 # 'YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM'.find('.')
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)

def ask_for_help(request):
    """
    user_input = {
        "client_name": "",
        "client_phone": "",
        "coc_location_id": ""
    }
    """
    #Attempt to find matching phone number. If none found, create new user.
    phone_number = ''.join([c for c in request.POST['client_phone'] if c in '1234567890'])
    existing_client = Client.objects.filter(phone_number=phone_number)
    if existing_client.exists():
        client_id = existing_client[0].id
    else:
        name_pieces = request.POST['client_name'].split(' ')
        first_name = name_pieces[0]
        last_name = ""
        if len(name_pieces) > 1:
            last_name = ' '.join(name_pieces[1:])
        new_c = Client(**{
            "first_name": first_name,
            "middle_name": "",
            "last_name": last_name,
            "phone_number": phone_number
        })
        new_c.save()
        client_id = new_c.id

    user_input = {
        "client_id": client_id,
        "coc_location_id": request.POST['coc_location_id'],
        "details": ""
    }
    user_input['referred_from_coc_location_id'] = -1 #From client
    user_input['event_type'] = "referral"
    Event(**user_input).save()

    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def log_note(request):
    """
    user_input = {
        "client_id": "",
        "coc_location_id": "",
        "details": ""
    }
    """
    user_input = json.loads(request.body)
    user_input['event_type'] = "note"
    Event(**user_input).save()

    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def grant_bed(request):
    """
    user_input = {
        "client_id": "",
        "coc_location_id": "",
        "details": ""
    }
    """
    user_input = json.loads(request.body)
    coc_loc = Coc.objects.get(id=user_input['coc_location_id'])
    user_input['event_type'] = "bed" if coc_loc.coc_type == "shelter" else "checkin"
    Event(**user_input).save()

    if coc_loc.coc_type == "shelter":
        coc_loc.beds_available = F('beds_available') - 1
        coc_loc.save()

    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def submit_referral(request):
    """
    user_input = {
        "client_id": "",
        "coc_location_id": "",
        "referred_from_coc_location_id": "",
        "details": ""
    }
    """
    user_input = json.loads(request.body)
    user_input['event_type'] = "referral"
    Event(**user_input).save()

    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def update_client_info(request):
    """
    user_input = {
        "phone_number": "",
        "first_name": "Robert",
        "last_name": "Hanks",
        "middle_name": "J",
        "pregnant": False,
        "dob": "1/1/1953",
        "gender": "Male",
        "veteran": True,
        "marital_status": "",
        "education": "",
        "sex_offender": False,
        "ssn": "100090077",
        "race": "Black",
        "number_of_children": 0,
        "id": 90077,
        "occupation": ""
    }
    """
    updates = json.loads(request.body)
    updates['phone_number'] = ''.join([c for c in updates['phone_number'] if c in '1234567890'])
    Client.objects.filter(id=updates['id']).update(**updates)

    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_client_info(request):
    """
    user_input = {
        "id": "3"
    }
    """
    user_input = json.loads(request.body)
    client_id = user_input['id']
    data = model_to_dict(Client.objects.get(id=client_id))
    data['events'] = []

    client_events = Event.objects.filter(client_id=client_id)

    coc_id_list = []
    client_id_list = []
    for ce in client_events:
        coc_id_list.append(ce.coc_location_id)
        client_id_list.append(ce.client_id)

    coc_name_lookup = {}
    for c in Coc.objects.filter(id__in=coc_id_list):
        coc_name_lookup[str(c.id)] = c.name

    client_deets_lookup = {}
    for c in Client.objects.filter(id__in=client_id_list):
        client_deets_lookup[str(c.id)] = {
            "name": c.first_name + " " + c.middle_name + " " + c.last_name,
            "phone_number": c.phone_number
        }

    for ce in client_events:
        ev = model_to_dict(ce)
        print "ev", ev
        ev['coc_name'] = coc_name_lookup[ev['coc_location_id']]
        ev['client_name'] = client_deets_lookup[ev['client_id']]['name']
        ev['client_phone_number'] = client_deets_lookup[ev['client_id']]['phone_number']
        data['events'].append(ev)

    return HttpResponse(json.dumps({
        "status": "success",
        "data": data
    }, default=json_custom_parser), content_type='application/json', status=200)

def get_clients(request):
    """
    user_input = {
        "phone_number": 3,
        "name": "bob"
    }
    """
    user_input = json.loads(request.body)

    results = []

    matches = {}

    name_pieces = user_input['name'].split(' ')
    first_name = name_pieces[0]
    last_name = name_pieces[-1]

    user_input['phone_number'] = ''.join([c for c in user_input['phone_number'] if c in '1234567890'])

    #Matching phone numbers
    if user_input['phone_number']:
        for c in Client.objects.filter(phone_number=user_input['phone_number']):
            if c.id not in matches: #block duplicates
                matches[c.id] = 1
                results.append(model_to_dict(c))

    #Matching Full Names
    for c in Client.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name):
        if c.id not in matches: #block duplicates
            matches[c.id] = 1
            results.append(model_to_dict(c))

    #Matching Last Names
    if last_name:
        for c in Client.objects.filter(last_name__iexact=last_name):
            if c.id not in matches: #block duplicates
                matches[c.id] = 1
                results.append(model_to_dict(c))

    #Matching First Names
    if first_name:
        for c in Client.objects.filter(first_name__iexact=first_name):
            if c.id not in matches: #block duplicates
                matches[c.id] = 1
                results.append(model_to_dict(c))

    return HttpResponse(json.dumps({
        "status": "success",
        "data": results
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_cocs(request):
    """
    user_input = {
        location:38.7315393, -90.6072538
        food:1
        law:1
        shelter:0
        housing:0
        medical:0
        status:single_male
        veteran:1
        pregnant:0
    }
    """
    try:
        user_input = json.loads(request.body)
    except:
        user_input = {}
        for k in request.POST.keys():
            user_input[k] = request.POST[k]

    coc_results = Coc.objects.all()
    if str(user_input['shelter']) == "0":
        coc_results = coc_results.exclude(coc_type="shelter")
    if str(user_input['food']) == "0":
        coc_results = coc_results.exclude(coc_type="food")
    if str(user_input['law']) == "0":
        coc_results = coc_results.exclude(coc_type="law")
    if str(user_input['housing']) == "0":
        coc_results = coc_results.exclude(coc_type="housing")
    if str(user_input['medical']) == "0":
        coc_results = coc_results.exclude(coc_type="medical")

    is_veteran = str(user_input['veteran']) == "1"
    is_pregnant = str(user_input['pregnant']) == "1"

    if user_input['status'] == "single_male":
        filtz = Q(allow_single_men=True)
        if is_veteran:
            filtz = filtz | Q(allow_veteran=True)
        coc_results = coc_results.filter(filtz)

    if user_input['status'] == "single_female":
        filtz = Q(allow_single_women=True)
        if is_pregnant:
            filtz = filtz | Q(require_pregnant=True)
        coc_results = coc_results.filter(filtz)

    if user_input['status'] == "family":
        coc_results = coc_results.filter(allow_family=True)

    results = []
    for c in coc_results:
        results.append(model_to_dict(c))

    return HttpResponse(json.dumps({
        "status": "success",
        "data": results
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_coc_info(request):
    """
    user_input = {
        "id": 3
    }
    """
    #user_input = json.loads(request.body)
    user_input = {
        "id": 10
    }

    data = Coc.objects.get(id=user_input['id'])
    data = model_to_dict(Coc.objects.get(id=user_input['id']))

    data['events'] = []

    client_events = Event.objects.filter(coc_location_id=user_input['id']).exclude(referred_from_coc_location_id=0)

    coc_id_list = []
    client_id_list = []
    for ce in client_events:
        coc_id_list.append(ce.coc_location_id)
        client_id_list.append(ce.client_id)

    coc_name_lookup = {}
    for c in Coc.objects.filter(id__in=coc_id_list):
        coc_name_lookup[str(c.id)] = c.name

    client_deets_lookup = {}
    for c in Client.objects.filter(id__in=client_id_list):
        client_deets_lookup[str(c.id)] = {
            "name": c.first_name + " " + c.middle_name + " " + c.last_name,
            "phone_number": c.phone_number
        }

    for ce in client_events:
        ev = model_to_dict(ce)
        print "ev", ev
        ev['coc_name'] = coc_name_lookup[ev['coc_location_id']]
        ev['client_name'] = client_deets_lookup[ev['client_id']]['name']
        ev['client_phone_number'] = client_deets_lookup[ev['client_id']]['phone_number']
        data['events'].append(ev)

    return HttpResponse(json.dumps({
        "status": "success",
        "data": data
    }, default=json_custom_parser), content_type='application/json', status=200)


def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")


@print_errors
def sms_received(request):

    #Automatically reset user's sessions if they haven't communicated in 5 minutes
    if 'last_validated' in request.session:

        session_expiry = (parser.parse(request.session.get('last_validated', '2000-01-01')) + datetime.timedelta(minutes=5))
        if session_expiry < datetime.datetime.now():
            print "Session expired! Session expiry time", session_expiry, " | current time", datetime.datetime.now()
            del request.session['last_validated']
            logout(request)
    else:
        request.session['last_validated'] = datetime.datetime.now().isoformat()

    input_from_user = request.POST.get('Body', '')

    if input_from_user.lower() == "restart":
        logout(request)

    if 'greeting' not in request.session:
        #New user!
        request.session['greeting'] = input_from_user
        twil = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Message method="GET">Need shelter for the night? We can help. Reply to this message with your current location (e.g. 911 Washington Ave, Saint Louis, MO 63304)</Message>
                </Response>
                '''
        return HttpResponse(twil, content_type='application/xml', status=200)
    elif 'location' not in request.session:
        request.session['location'] = input_from_user
        twil = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Message method="GET">Reply to this with a number 1-3 corresponding to what best describes you. Are you a single male (1), a single female (2), or a family (3)?</Message>
                </Response>
                '''
        return HttpResponse(twil, content_type='application/xml', status=200)
    elif 'status' not in request.session:
        if input_from_user == '1':
            request.session['status'] = "single_male"
        elif  input_from_user == '2':
            request.session['status'] = "single_female"
        elif  input_from_user == '3':
            request.session['status'] = "family"
        else:
            twil = '''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                        <Message method="GET">Invalid response, must reply with a number 1-3. Are you a single male (1), a single female (2), or a family (3)?</Message>
                    </Response>
                    '''
            return HttpResponse(twil, content_type='application/xml', status=200)

        twil = '''<?xml version="1.0" encoding="UTF-8"?>
                <Response>
                    <Message method="GET">Reply to this with a number 1-3 corresponding to what best describes you. Are you a veteran (1), pregnant (2), or neither (3)?</Message>
                </Response>
                '''
        return HttpResponse(twil, content_type='application/xml', status=200)

    elif 'special_status' not in request.session:

        if input_from_user == '1':
            request.session['special_status'] = "veteran"
        elif  input_from_user == '2':
            request.session['special_status'] = "pregnant"
        elif  input_from_user == '3':
            request.session['special_status'] = "none"
        else:
            twil = '''<?xml version="1.0" encoding="UTF-8"?>
                    <Response>
                        <Message method="GET">Invalid response, must reply with a number 1-3. Are you a veteran (1), pregnant (2), or neither (3)?</Message>
                    </Response>
                    '''
            return HttpResponse(twil, content_type='application/xml', status=200)

    #Find best matching CoC
    #Todo add filters for single male/female/vet etc
    #Todo add filter by distance from location
    best_shelter = Coc.objects.filter(coc_type="shelter").order_by('?')[0]

    twil = '<?xml version="1.0" encoding="UTF-8"?> \
            <Response> \
                <Message method="GET">Your best bet is '+best_shelter.name+', located at '+best_shelter.address+'. Their phone number is '+best_shelter.phone_number+' and they currently have '+str(best_shelter.beds_available)+' beds available.</Message> \
            </Response> \
            '
    return HttpResponse(twil, content_type='application/xml', status=200)
