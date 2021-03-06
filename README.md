# DataVis
Data Visualization tool using Django Postgres and Bootstrap

Link to Youtube video demo - https://youtu.be/JXux9O9-UsE   <br>

<H3># Data Visualization project for CitiBike Trip Dataset</H3>

<H4> Technologies Used:</H4>
- Backend - Python, Django, Docker, PostgreSQL <br>
- Frontend - Bootstrap, Js, HTML, CSS <br>
- API - Google Charts (Chart Js), MapBox <br>

<br>

Dataset - https://www.citibikenyc.com/system-data <br>
About the data - Where do Citi Bikers ride? When do they ride? How far do they go? Which stations are most popular? What days of the week are most rides taken on?
<br>
<br>
The data includes:

    Trip Duration (seconds)
    Start Time and Date
    Stop Time and Date
    Start Station Name
    End Station Name
    Station ID
    Station Lat/Long
    Bike ID
    User Type (Customer = 24-hour pass or 3-day pass user; Subscriber = Annual Member)
    Gender (Zero=unknown; 1=male; 2=female)
    Year of Birth

This data has been processed to remove trips that are taken by staff as they service and inspect the system, trips that are taken to/from any of our “test” stations (which we were using more in June and July 2013), and any trips that were below 60 seconds in length (potentially false starts or users trying to re-dock a bike to ensure it's secure). <br> <br>

The current view of the Application - <br>
- Subscriber Type Bar Chart
- Top k Start/End Stations by trip count on a Map
- Selected Station’s sum of trip count during each hour of the day bar chart.

<img src = "https://github.com/Abhis33/DataVis/blob/master/img1.png">



