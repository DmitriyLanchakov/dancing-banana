import os, sys
import csv

os.environ['DJANGO_SETTINGS_MODULE'] = 'hackathon.settings'
import django
django.setup()

if os.environ.get('IS_HEROKU_SERVER', False):
    pass
else:
    #local
    try:
        os.system("rm db.sqlite3") #Kill existing db
    except:
        pass

os.system("python manage.py migrate") #Create new db


from api.models import Client
from dateutil import parser

print "~~~~~~~~~~~~~~~~~"
with open('clients.csv', 'rb') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i +=1
        if i > 1:
            drivers_license_number_phone = ""
            race = "Unknown"
            if row[9] != '0':
                race = "Native American"
            if row[10] != '0':
                race = "Asian"
            if row[11] != '0':
                race = "Black"
            if row[12] != '0':
                race = "Pacific Islander"
            if row[13] != '0':
                race = "White"
            gender = "Male"
            if row[16] != '0':
                gender = "Female"
            new_client = Client(**{
                "id": int(row[0]),
                "first_name": row[1],
                "middle_name": row[2],
                "last_name": row[3],
                "ssn": row[5],
                "dob": row[7],
                "race": race,
                "gender": gender,
                "veteran": True if row[17] == '1' else False,
            })
            new_client.save()
    print "Imported", i, "clients."


if os.environ.get('IS_HEROKU_SERVER', False):
    pass
else:
    #local
    os.system("python manage.py loaddata fixtures/superuser.json")
