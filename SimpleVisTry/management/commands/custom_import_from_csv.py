from SimpleVisTry.models import CitiBike
from django.core.management.base import BaseCommand
import pandas as pd


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        #insert_count = CitiBike.objects.from_csv('201912-citibike-tripdata.csv')

        df = pd.read_csv('201912-citibike-tripdata.csv')

        df = df.rename(columns={'start station id': 'start_station_id', 'start station name': 'start_station_name', 'start station latitude': 'start_station_latitude', 'start station longitude': 'start_station_longitude', 'end station id': 'end_station_id', 'end station name': 'end_station_name', 'end station latitude': 'end_station_latitude', 'end station longitude': 'end_station_longitude', 'birth year': 'birth_year'})

        df['starttime'] = pd.to_datetime(df['starttime'])
        df['stoptime'] = pd.to_datetime(df['stoptime'])

        k = 0

        while (k < len(df)):

            CitiBike.objects.bulk_create(
                CitiBike(**vals) for vals in df.iloc[k:k+100].to_dict('records')
            )

            k = k+100

        print("Done all!")
