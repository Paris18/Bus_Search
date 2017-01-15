from django.shortcuts import render
from datetime import datetime,timedelta
from .models import Buses,Seats
from django.http import HttpResponse,HttpResponseRedirect
import random

# Create your views here.
name = ["vrl","srs","kadamba","bharati"]
bus_from = ["belgavi","vijaypur","hulbi","kalburgi"]
bus_to = ["benglore","mysore","shivamogga","tumkure"]
bus_type = ["ac sleeper","ac non-sleeper","non-ac sleeper","non-ac non-sleeper"]
time = datetime.now()


def addlist(request):
	# print time
	# n = Buses.objects.count()
	# for i in range (0, 200):
	# 	n += 1
	# 	obj = Buses(bus_id = n, name = name[random.randint(0,3)],bus_from = bus_from[random.randint(0,3)],bus_to = bus_to[random.randint(0,3)],arrival_time = time +timedelta(hours = i),price = random.randint(499,999),departure_time = time +timedelta(hours = i+6),no_seats = 40,total_seats = 40,available_seats = 40,bus_type = bus_type[random.randint(0,3)]) 
	# 	obj.save()
	return HttpResponse(Buses.objects.count())

def seatlist(request):
# 	seat_typ = ["GEN","LDS"] 
# 	window = ["True","False"]
# 	Seats.objects.all().delete()
# 	for i in range (1,(Buses.objects.count() + 1 )):
# 	 	n = Buses.objects.get(bus_id = i)
# 	 	print n.bus_id
# 	 	for j in range(1,n.total_seats+1):
# 	 		seat_nom = "S_" + chr(j)
# 	 		n.seats_set.create(seat_status = "Available",seat_no = seat_nom ,seat_type =seat_typ[random.randint(0,1)], window_seat = window[random.randint(0,1)])				
	return HttpResponse(Seats.objects.count())

	