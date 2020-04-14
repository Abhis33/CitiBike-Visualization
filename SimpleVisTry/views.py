from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.db.models import Count
from django.contrib.auth.models import User
from .models import CitiBike

# Create your views here.
def home(request):
    print("Heyy")
    return render(request, 'home.html')

class subscriber_data(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        values = [each['id__count'] for each in (CitiBike.objects.values("usertype").annotate(Count("id")))]
        subscriber_type = [CitiBike['usertype'] for CitiBike in CitiBike.objects.values('usertype').distinct()]
        data = {
            "default" : values,
            "subscriber_type" : subscriber_type
        }
        print(data)
        return Response(data)
