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


def ask_for_help(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def log_note(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def grant_bed(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def submit_referral(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)

def update_client_info(request):
    return HttpResponse(json.dumps({
        "status": "success"
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_client_info(request):
    # client_id = request.GET['client_id']
    # client_info = Client.objects.filter(id=client_id)
    # client_events = Event.objects.filter(client_id=client_id)

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
            "client_id": 14,
            "details": "Given Bed",
            "created": datetime.datetime.now()
        },
        {
            "coc_location_name": "Urgent Care",
            "coc_id": "2",
            "event_type": "referral",
            "client_id": 13,
            "details": "Please assist this person, they need help",
            "created": datetime.datetime.now()
        },
        {
            "coc_location_name": "Night Shelter",
            "coc_id": "12",
            "event_type": "note",
            "client_id": 12,
            "details": "Note that upon a discussion with this person, we found out they have extensive experience in the food service industry",
            "created": datetime.datetime.now()
        }
    ]

    data = random.choice(client_info)
    data['events'] = client_events

    return HttpResponse(json.dumps({
        "status": "success",
        "data": data
    }, default=json_custom_parser), content_type='application/json', status=200)

def get_clients(request):

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

    return HttpResponse(json.dumps({
        "status": "success",
        "data": client_info
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_cocs(request):

    coc_info = [
        {
            "name": "Shelter Nightly",
            "address": "360 Calmgrove Ave, Saint Louis, MO 63101",
            "latitude": "35.6894",
            "longitude": "139.692",
            "phone_number": "(909) 790-2903",
            "beds_available": "80",
            "beds_total": "100"
        },
        {
            "name": "Medical Place",
            "address": "360 Calmgrove Ave, Saint Louis, MO 63101",
            "latitude": "35.8894",
            "longitude": "139.692",
            "phone_number": "(909) 790-2903",
            "beds_available": "0",
            "beds_total": "0"
        }
    ]

    return HttpResponse(json.dumps({
        "status": "success",
        "data": coc_info
    }, default=json_custom_parser), content_type='application/json', status=200)


def get_coc_info(request):

    coc_info = [
        {
            "name": "Shelter Nightly",
            "address": "360 Calmgrove Ave, Saint Louis, MO 63101",
            "latitude": "35.6894",
            "longitude": "139.692",
            "phone_number": "(909) 790-2903",
            "beds_available": "80",
            "beds_total": "100"
        },
        {
            "name": "Medical Place",
            "address": "360 Calmgrove Ave, Saint Louis, MO 63101",
            "latitude": "35.8894",
            "longitude": "139.692",
            "phone_number": "(909) 790-2903",
            "beds_available": "0",
            "beds_total": "0"
        }
    ]

    return HttpResponse(json.dumps({
        "status": "success",
        "data": random.choice(coc_info)
    }, default=json_custom_parser), content_type='application/json', status=200)


def load_frontend(request):
    return HttpResponseRedirect("/static/index.html")
