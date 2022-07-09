from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()
client.login(username='carefi', password='asd@1234')
client.get('/getbtc/')
