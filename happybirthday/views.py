from django.http import HttpResponse
from django.shortcuts import render

from .models import Doctor

import datetime, pytz

# Create your views here.
def home(request):
    current_user = Doctor.objects.get(username="tomwerner")
    content = {'todays_birthday_list': get_todays_birthdays(current_user.doctor_id)}
    return render(request, 'happybirthday/home.html', content)

def get_todays_birthdays(doctor_id):
    current_time = datetime.datetime.now(pytz.utc) #TODO: Figure out timezone stuff? maybe https://gun.io/blog/django-easy-timezones/

    # TODO: do request

    # TODO: get useful information out of request

    return [
        {'name': 'Abby Doe', 'gender': 'Female', 'age': 50, 'cell_phone': '123-456-1234'},
        {'name': 'Bob Doe', 'gender': 'Male', 'age': 25},
        {'name': 'Cathy Doe', 'gender': 'Female', 'age': 33},
        {'name': 'Doug Doe', 'gender': 'Male', 'age': 40, 'cell_phone': '432-456-3422'},
    ]