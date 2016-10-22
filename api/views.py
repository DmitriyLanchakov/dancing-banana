from django.http import HttpResponse
import datetime
import json
from api.models import Client, Event, Coc
from django.http import HttpResponseRedirect
import collections
from decimal import Decimal
from django.forms.models import model_to_dict
from django.db.models import F

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
        "client_id": "",
        "coc_location_id": "",
        "details": ""
    }
    """
    user_input = request.body
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
    user_input['event_type'] = "shelter"
    Event(**user_input).save()

    coc_loc = Coc.objects.get(id=user_input['coc_location_id'])
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
    client_info = Client.objects.get(id=client_id)
    client_events = Event.objects.filter(client_id=client_id)

    data = model_to_dict(client_info)
    data['events'] = client_events

    return HttpResponse(json.dumps({
        "status": "success",
        "data": data
    }, default=json_custom_parser), content_type='application/json', status=200)

def get_clients(request):
    #todo add filters
    results = []
    for c in Client.objects.all():
        results.append(model_to_dict(c))

    return HttpResponse(json.dumps({
        "status": "success",
        "data": results
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_cocs(request):
    #Todo, add filters
    results = []
    for c in Coc.objects.all():
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
    user_input = json.loads(request.body)

    data = Coc.objects.get(id=user_input['coc_location_id'])

    return HttpResponse(json.dumps({
        "status": "success",
        "data": model_to_dict(data)
    }, default=json_custom_parser), content_type='application/json', status=200)


def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")
