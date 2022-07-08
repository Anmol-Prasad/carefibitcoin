from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('getbtc/', views.getdata, name="getdata"),
    path('login/', views.logindata, name="login")
]
