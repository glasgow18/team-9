import json
from urllib.request import urlopen
#from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
#from codeforgood.models import Users, Locations, Tags, Location_Tags, Favourites, Saved_Searches
#from django.contrib.auth import authenticate, login
#from django.core.urlresolvers import reverse
#from django.shortcuts import render
#from social.forms import RegistrationForm, UserProfileForm
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
import django
django.setup()
from codeforgood.models import Locations, Tags, Location_Tags, Categories
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import datetime
#from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from math import sin, cos, sqrt, atan2, radians
# import re
# approximate radius of earth in km


def getLocation():


    url = 'http://ipinfo.io?token=b4c8c534242400'
    response =urlopen(url)
    data = json.load(response)
    loc = data['loc']
    return loc

def calculateDistance():
    location = getLocation().split(',')
    R = 6373.0
    lat1 = radians(float(location[0]))
    lon1 = radians(float(location[1]))
    lat2 = radians(56)
    lon2 = radians(-4)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def index(request):
    return render(request, 'index.html')

def add_location(request):
    return render(request, 'add_location.html')

def search(request):
    input = request.GET.get('name','')
    good_input = input.split()
    categories = Categories.objects.all()
    tags_location = Location_Tags.objects.all()               #
    tags_list = []
    tags_final = []
    locations = Locations.objects.all()
    results = []
    if (good_input[0] != ""):
        for input in good_input:
            tags_list.append(input)
            for tag in categories:
                if(input.lower() == tag.subcategory.lower()):
                    tags_list.append(tag.category)
        for tag in tags_list:
            for tag_loc in tags_location:
                if(tag == tag_loc.tag):
                    tags_final.append(tag_loc)
        for location in locations:
            islocation = False
            for input in good_input:
                if(location.name.lower().find(input.lower()) != -1):
                    results.append(location)
                    islocation = True
                    break
            if(not islocation):
                valid = False
                for tag in tags_final:
                    if(tag.location == location):
                        results.append(location)
                        valid = True
                        break
                if(not valid):
                    for input in good_input:
                        if(location.description.lower().find(input.lower()) != -1):
                            results.append(location)
                            break;

        return render(request, "search.html", {"locations":results, "search":request.GET.get("name","")})
    else:
        return locations

def list_loc_by_distance():
    distances = []
    array = []
    #locations = search()
    for location in locations:
        distances.append(calculateDistance(location.latitude,location.longitude))
    for x in range(0,len(distances)):
        if(distances[x] > 20):
            distances.remove(x)
            locations.remove(x)
            --x
    for y in range(len(distances)):
        array.append([locations[y]],[distances[y]])


def addLocation(request):

    loc_name = request.GET.get('name')
    loc_place = request.GET.get('place')
    loc_description = request.GET.get('description')
    if(loc_name and loc_place and loc_description ):
        return django.http.HttpResponseBadRequest()
    loc_date = request.GET.get('date', "")
    lan = request.GET.get('name',"")
    lon= request.GET.get('name',"")
    contact_name= request.GET.get('name',"")
    contact_num = request.GET.get('name',"")
    contact_email = request.GET.get('name',"")
    website = request.GET.get('website',"")
    cost = request.GET.get('cost',"")
    user = request.GET.get('user', "NULL")
    location = Locations.objects.get_or_create(loc_name,lan,lon,loc_place,contact_name,contact_num,contact_email,website,cost,loc_description,loc_date,user)[0]
    location.save()









