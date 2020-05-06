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
        qry = CitiBike.objects.values("usertype").annotate(Count("id"))

        values = [each['id__count'] for each in (qry)]
        subscriber_type = [each['usertype'] for each in (qry)]
        data = {
            "default" : values,
            "subscriber_type" : subscriber_type
        }

        return Response(data)

class top_k_start_stn(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, k = 5,format=None):
        stn_obj = CitiBike.objects.values("start_station_id","start_station_name","start_station_latitude","start_station_longitude").annotate(Count("id")).order_by('-id__count')[:k]

        #Need these stuff to plot on map
        #start_station_id
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

class top_k_end_stn(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, k = 5, format=None):

        stn_obj = CitiBike.objects.values("end_station_id","end_station_name","end_station_latitude","end_station_longitude").annotate(Count("id")).order_by('-id__count')[:k]

        #Need these stuff to plot on map
        #end_station_id
        #end_station_name
        #end_station_latitude
        #end_station_longitude

        ######################## GeoJson Conversion code
        geo_json = [ {"type": "Feature",
                    "properties": {
                        "id":  each['end_station_id'],
                        "name": each['end_station_name'],
                        "Count": each['id__count'],
                        "popupContent":  "id=%s" % (each['end_station_name'],)
                        },
                    "geometry": {
                        "type": "Point",
                        "coordinates": [ each['end_station_longitude'],each['end_station_latitude'] ] }}
                    for each in stn_obj ]

        ####--------

        return Response(geo_json)

class hourly_avg_stn_trip_count(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, stn_id = -999 , format=None):

        if (stn_id == -999):
            stn_id = CitiBike.objects.values("start_station_id").annotate(Count("id")).order_by('-id__count')[0]['start_station_id']
            print("Default Station Id set to Top Start Station - "+str(stn_id))

        tmp = CitiBike.objects.filter(start_station_id = stn_id)
        stn_obj = tmp.values("starttime__hour").annotate(Count("id")).order_by('starttime__hour')

        count_lst = [each['id__count'] for each in stn_obj]
        hour_lst = [each['starttime__hour'] for each in stn_obj]

        data = {
            "default" : count_lst,
            "hour" : hour_lst
        }

        return Response(data)
