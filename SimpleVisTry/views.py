from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import CitiBike

# Create your views here.
def home(request):
    print("Heyy")
    return render(request, 'home.html')

class DBData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = [CitiBike['usertype'] for CitiBike in CitiBike.objects.values('usertype').distinct()]
        print(data)
        return Response(data)
