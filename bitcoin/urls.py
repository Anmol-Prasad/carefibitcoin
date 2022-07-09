from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    # URL for homepage
    path('', views.index, name="index"),
    # URL to fetch data for AUTHENTICATED users using GET request
    path('getbtc/', views.getdata, name="getdata"),
    # URL for the login page
    path('login/', views.logindata, name="login")
]
