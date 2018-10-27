from django.shortcuts import render
from codeforgood.models import Locations
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html')


def search_dummy(request):
    if request.method == 'GET':
        status = Locations.objects.filter(id__lt=5)
        return render(request,"search.html", {"locations":status})


