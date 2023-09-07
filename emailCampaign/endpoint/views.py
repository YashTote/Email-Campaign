from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csfr_exempt
from .models import *
# Create your views here

def send_email():
    mail_data = Campaign.objects.all()
    users = Subscriber.objects.all()

    