from django.http import HttpResponse
import requests
from django.shortcuts import render, redirect
from .models import Coindata
from datetime import datetime
from django.contrib.auth import authenticate


# THIS FUNCTION WILL FETCH LIVE BITCOIN PRICE provided by Coingecko API and POST the required contents (name, timestamp, current price) on the database


def index(request):
    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()

    if request.method == "POST":
        name = request.POST['name']
        symbol = request.POST['symbol']
        price = request.POST['price']
        newtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cdata = Coindata(name=name, symbol=symbol,
                         price=price, newtime=newtime)
        cdata.save()
    return render(request, ('index.html'), {'apidata': apidata})


# THIS FUNCTION WILL FETCH THE LIST OF ALL BITCOIN PRICES STORED IN DATABASE TABLE using GET request but it would only work if the user is authenticated or else would return 401 Http Response


def getdata(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    else:
        allData = Coindata.objects.all()
        print(allData)
        return render(request, ('btcdata.html'), {"datas": allData})


# THIS FUNCTION WILL ALLOW REGISTERED USERS TO LOGIN INTO THE SITE
def logindata(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print('Authenticated')
        else:
            print('Not')
    return render(request, 'login.html')
