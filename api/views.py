from django.http import HttpResponse
import datetime
import json
from api.models import Client, Event
from django.http import HttpResponseRedirect
import random

def json_custom_parser(obj):
    if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        dot_ix = 19
        return obj.isoformat()[:dot_ix]
    else:
        raise TypeError(obj)

"""
    url(r'^get_client_info$', "api.views.get_client_info"),
    url(r'^update_client_info$', "api.views.update_client_info"),
    url(r'^get_cocs$', "api.views.get_cocs"),
    url(r'^ask_for_help$', "api.views.ask_for_help"),
    url(r'^search$', "api.views.search"),
    url(r'^log_note$', "api.views.log_note"),
    url(r'^get_coc_info$', "api.views.get_coc_info"),
    url(r'^grant_bed$', "api.views.grant_bed"),
    url(r'^submit_referral$', "api.views.submit_referral"),
"""

def get_client_info(request):
    client_id = request.GET['client_id']
    client_info = Client.objects.filter(id=client_id)
    client_events = Event.objects.filter(client_id=client_id)

    client_info = [
        {
            "name": "Joe Bob",
            "phone_number": "(909) 790-7900",
            "ssn": "633 64 6333",
            "dob": "10/31/1933",
            "gender": "Male",
            "pregnant": False,
            "race": "Asian",
            "marital_status": "Single",
            "number_of_children": 0,
            "veteran": True,
            "occupation": "Sheet Metal Worker",
            "education": "Masters in Sheet Metal",
            "sex_offender": False
        },
        {
            "name": "Sally Sally",
            "phone_number": "(909) 790-7900",
            "ssn": "633 64 6333",
            "dob": "10/31/1933",
            "gender": "Female",
            "pregnant": True,
            "race": "African American",
            "marital_status": "Married",
            "number_of_children": 2,
            "veteran": False,
            "occupation": "Mother",
            "education": "High School",
            "sex_offender": False
        }
    ]

    client_events = [
        {
            "coc_location_name": "Night Shelter",
            "coc_id": "12",
            "event_type": "shelter",
            "client_id": client_id,
            "details": "Given Bed",
            "created": datetime.datetime.now()
        },
        {
            "coc_location_name": "Urgent Care",
            "coc_id": "2",
            "event_type": "referral",
            "client_id": client_id,
            "details": "Please assist this person, they need help",
            "created": datetime.datetime.now()
        },
        {
            "coc_location_name": "Night Shelter",
            "coc_id": "12",
            "event_type": "note",
            "client_id": client_id,
            "details": "Note that upon a discussion with this person, we found out they have extensive experience in the food service industry",
            "created": datetime.datetime.now()
        }
    ]
    return HttpResponse(json.dumps({
        "status": "success",
        "data": {
            "client_info": random.choice(client_info),
            "client_events": client_events
        }
    }, default=json_custom_parser), content_type='application/json', status=200)



def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")
