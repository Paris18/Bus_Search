from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.

class Buses(models.Model):
	bus_id = models.CharField(max_length = 10,primary_key = True)
	name = models.CharField(max_length = 100,blank = False)
	bus_from = models.CharField(max_length = 25,blank = False)
	bus_to = models.CharField(max_length = 25,blank = False)
	arrival_time = models.TimeField(blank = False)
	price= models.IntegerField(default = 10,blank = False)
	departure_time = models.TimeField(blank = False)
	no_seats = models.IntegerField(blank = False)
	total_seats = models.IntegerField(default = 0,blank = False)
	available_seats = models.IntegerField(default = 0,blank = False)
	bus_type = models.CharField(default = None ,max_length = 50 , blank = False)



class Seats(models.Model):
	bus_id = models.ForeignKey(Buses)
	seat_status =models.CharField(max_length = 50 , blank = False)
	seat_no = models.CharField(max_length = 5, blank = False)
	seat_type = models.CharField(max_length = 20 , blank = False)
	window_seat = models.BooleanField(default = False)


