from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import Users,Example
from busside.models import Buses,Seats
import json
import datetime
from datetime import datetime,timedelta
import requests
from datetime import date
from django.template.response import TemplateResponse
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage





# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['to@example.com'],
#     fail_silently=False,
# )
# Create your views here.


# def crtable(request):
	# for i in range(0,10):
		# d = User(question_text = get_random_string(length=2, allowed_chars='ACTGNKVIO'))
		# print d.question_text
		# d.save()
	# return HttpResponse("no of records is "+str(Question.objects.count()))

def signup(request):
	if request.method == 'GET':
		return render(request, "name.html",{})
	if request.POST:
		namec = request.POST['name']
		# dt = request.POST['DOB']
		dt = datetime.datetime.strptime(request.POST['DOB'], "%Y-%m-%d").date()
		adress = request.POST['adress']
		email_id = request.POST['email']
		password = request.POST['password']
		mob_nom = request.POST['mob_no']
		today = date.today()
		ageb = today.year - dt.year -((today.month, today.day) < (dt.month, dt.day))
		print ageb
		# print request.form
		# data = json.loads(request.body)
		# print data
		if(len(namec) == 0 or len(adress) == 0 or len(email_id) == 0 or len(password) == 0):
			return render_to_response('alertmessage.html',{"message" :'all feilds are neccesory'})
		if Users.objects.filter(name = namec,passwrd = password).exists():
			return HttpResponse("account already exists")
		else:
			d = Users(name = namec, DOB = dt, age = ageb, address = adress, mob_no = mob_nom, email = email_id, passwrd = password)
			d.save()
			email = EmailMessage('bus signup','your successfully signed up',[email_id])
			email.send()
			return HttpResponse("done")


def bussearch(request):
	# if request.POST:
	print "hi"
	From = request.POST['from']
	To = request.POST['to']
	# print From,To
	deprt_time = request.POST['Dd']
	Arival_time = datetime.now() + timedelta(hours = 1)
	buses = Buses.objects.filter(bus_from = From, bus_to = To, arrival_time__gte = Arival_time)
	print buses.count()
	bus_data = {}
	for b in buses:
		bus_data[b.bus_id] = {'name':b.name, 'bus_from':b.bus_from ,'bus_to':b.bus_to ,'arrival_time':str(b.arrival_time), 'price':b.price ,'departure_time':str(b.departure_time) ,'available_seats':b.available_seats ,'bus_type':b.bus_type}
	
	print "hi"
	return render(request, "bookticket.html",{'data':json.dumps(bus_data)})	         
	# return HttpResponse("hi")



log_in_bool = False
def login(request):
	if request.method == 'GET':
		return render(request, "login.html",{})
	if request.POST:
		namev = request.POST['user_name']
		password = request.POST['password']
		if Users.objects.filter(name = namev,passwrd = password).exists():
			log_in = True
			# email = EmailMessage('test', 'Body', to=['pariskamal8@gmail.com'])
			# email.send()
			return render(request, "page1.html",{})
		else:
			return HttpResponse("wrong login")


def logout(request):
	print"hi"
	if log_in_bool == True:
		log_in_bool =False
		return HttpResponseRedirect("app1/login")

# def seat_book(request):


def seat_list(request):
	bus_ID = request.POST['bus_no']
	price = request.POST['price']
	print Seats.objects.all(bus_id = bus_ID)
	

def select_seat(request):
	bus_ID = request.POST['bus_no']
	seat_No = request.POST['seat_no']
	price = request.POST['price']
	d = Seats.objects.filter(bus_id = bus_ID,seat_no = seat_No)
	d.update(seat_status = "BUSY")
	seat_dict = {}
	seat_dict['id'] = d.bus_id
	seat_dict['seat_type'] = d.seat_type
	seat_dict['seat_no'] = d.seat_no
	seat_dict['window_seat'] = d.window_seat
	seat_dict['price'] = price
	data = json.dumps(seat_dict)
	return render(request, "bookticket.html",{'seat_info': data })

def book_ticket(request):
	bus_ID = request.POST['bus_no']
	seat_Id = request.POST['seat_no']
	Seats.objects.filter(bus_id = bus_ID , seat_no = seat_Id).update("BOOKED")
	Buses.objects.filter(bus_id = bus_ID)
	d.update(available_seats = d.available_seats-1)






# return HttpResponse(json.dumps(response_data), content_type="application/json")




