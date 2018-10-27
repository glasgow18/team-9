from django.shortcuts import render
from models import Locations
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html')


def search_dummy(request):
    if request.method == 'GET':
        status = Locations.objects.filter(id < 5)
        return render(request,"search.html", {"locations":status})
