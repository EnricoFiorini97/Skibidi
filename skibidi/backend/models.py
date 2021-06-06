from django.db import models
from address.models import AddressField
#TODO:Set max integer

class Clients(models.Model):
    name = models.CharField(max_length = 255, null=False)
    surname = models.CharField(max_length = 255, null=False)
    social_security_number = models.CharField(max_length=16, primary_key=True)

class Booking(models.Model):
    class Meta:
        unique_together = (('client_id', 'hotel_id', 'room_id'),)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    client_id = models.CharField(max_length=16, null=False)
    hotel_id = models.CharField(max_length=16, null=False)
    room_id = models.PositiveSmallIntegerField(null=False)
    
class Hotels(models.Model):
    vat_number = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length = 255)
    total_rooms = models.PositiveSmallIntegerField(null=False)
    available_rooms = models.PositiveSmallIntegerField(null=False)
    rating_system =  models.PositiveSmallIntegerField(null=False)
    address = AddressField()

class Rooms(models.Model):
    room_id = models.PositiveSmallIntegerField(null=False)
    beds = models.PositiveSmallIntegerField(null=False)
    available = models.BooleanField(null=False)

class Review(models.Model):
    class Meta:
        unique_together = (('client_id', 'hotel_id'),)
    client_id = models.CharField(max_length=16, null=False)
    hotel_id = models.CharField(max_length=16, null=False)
    rating = models.PositiveSmallIntegerField(null=False)
    text_review =  models.CharField(max_length=4000)