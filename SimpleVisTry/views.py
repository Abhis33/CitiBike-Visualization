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

        print("")
        print(data)
        return Response(data)

class top_k_start_stn(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        k = 5
        stn_obj = CitiBike.objects.values("start_station_id","start_station_name","start_station_latitude","start_station_longitude").annotate(Count("id")).order_by('-id__count')[:k]

        #Need these stuff to plot on map
        #start_station_id = []
        #start_station_name
        #start_station_latitude
        #start_station_longitude

        ######################## GeoJson Conversion code
        geo_json = [ {"type": "Feature",
                    "properties": {
                        "id":  each['start_station_id'],
                        "name": each['start_station_name'],
                        "Count": each['id__count'],
                        "popupContent":  "id=%s" % (each['start_station_name'],)
                        },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [ each['start_station_longitude'],each['start_station_latitude'] ] }}
                    for each in stn_obj ]

        ####--------

        return Response(geo_json)
