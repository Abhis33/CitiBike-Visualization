"""DataVisServerDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SimpleVisTry import views
from SimpleVisTry.views import subscriber_data, top_k_start_stn, top_k_end_stn, hourly_avg_stn_trip_count

urlpatterns = [
    path('', views.home, name='home'),
    path('api/subscriber_data/', subscriber_data.as_view(), name='home'),

    path('api/top_k_start_stn/', top_k_start_stn.as_view(), name='home'),
    path('api/top_k_start_stn/<int:k>/', top_k_start_stn.as_view(), name='home'),

    path('api/top_k_end_stn/', top_k_end_stn.as_view(), name='home'),
    path('api/top_k_end_stn/<int:k>/', top_k_end_stn.as_view(), name='home'),

    path('api/hourly_avg_stn_trip_count/', hourly_avg_stn_trip_count.as_view(), name='home'),
    path('api/hourly_avg_stn_trip_count/<int:stn_id>/', hourly_avg_stn_trip_count.as_view(), name='home'),

    path('admin/', admin.site.urls),
]
