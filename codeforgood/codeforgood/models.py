from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.DateTimeField()

class Locations(models.Model):
    name = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    tags = models.CharField(max_length=4095)
    accessbility = models.CharField(max_length=4095)
    date = models.DateField()
    user_id = models.ForeignKey(Users, on_delete = models.SET_NULL, null = True, default = None)

    def __str__(self):
        return self.name

class Favourites(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.SET_NULL, null = True, default = None)
    favourite_loc_id = models.ForeignKey(Locations, on_delete = models.SET_NULL, null = True, default = None)

class Saved_Searches(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.SET_NULL, null = True, default = None)
    location = models.CharField(max_length=255)
    search = models.CharField(max_length=255)
search_filters = models.CharField(max_length=255)

class Suggestions(models.Model):
    loc_id = models.ForeignKey(Locations, on_delete = models.SET_NULL, null = True, default = None)
    user_id = models.ForeignKey(Users, on_delete = models.SET_NULL, null = True, default = None)
    suggestion = models.CharField(max_length=6000)

class Warnings(models.Model):
    loc_id = models.ForeignKey(Locations, on_delete = models.SET_NULL, null = True, default = None)
    warning = models.CharField(max_length=255)

class Categories(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    
