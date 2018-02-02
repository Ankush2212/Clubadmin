import requests
from django.conf import settings
#from django.core.mail import send_mail
from django.contrib import messages
import smtplib
from django.contrib.sessions.models import Session
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import datetime
#from datetime import timedelta

from .models import singleservice 
from .models import adduser 
from .models import fulliteservice 
from .models import hotelservice 
from .models import adminsignup 
from .models import employeedetail 
from .models import pricingplan 

#from datetime import datetime,timedelta
#from time import strftime
from django.conf.urls import include, url


from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    #return HttpResponse('Hefdd gfdgdf llo fddcccx xczfddvd x dddrom Python!')
	# services = Hotelservice.objects.all()
	 return render(request, 'index.html')
	 
##############Onze-prijzen//////////////////////////	 
def onzeprijzen(request):
    return render(request, 'onzeprijzen.html')


def login1(request):
	username = 'not logged in'
	first_name = ''
	password = ''
	existid = ''
	#return HttpResponse('hello')
	getsession = request.session.get('id')=='None'
	if request.session.get('id')=='None':
		redirect(login1)
	else:
	
		if request.method == 'POST':
			first_name = request.POST.get('first_name')
			password = request.POST.get('password')
			getw =  Signup.objects.filter(first_name=first_name,password=password).order_by('-id')[:1]
			#return HttpResponse("name")
			for i in getw:
				existid = i.id
				if existid: 
					request.session['id'] = existid
					return redirect(welcome)
				else:
					# #request.session['error'] = 'User not identified'
					return redirect(login1)
				
	return render(request, 'login.html') 
		
def welcome(request):
	getsession = request.session.get('id')
	if getsession:
		getrecord =  Signup.objects.get(id=getsession)
		return render(request, 'welcome.html',{'form':getrecord}) 
	else:
		return redirect(login1)


def logout1(request):
	try:
		del request.session['id']
	except KeyError:
		return HttpResponse("You're logged out.")
	return redirect(login1)



#backed login

def addadmindetails(request):

	adminsignup1 = adminsignup()
	adminsignup1.firstname='admin'
	#adminsignup1.lastname='admin'
	adminsignup1.email='admin@gmail.com'
	adminsignup1.password='admin@123' 
	adminsignup1.save()
	#contacts = adminsignup.objects.all()
	return HttpResponse("You're logged out.")
	#return render(request)
	
##################################backed login##############################################
def admin(request):
	username = ''
	password = ''
	existid = ''
	#request.session['error']=""
	#error = request.session.get('error')
	
	#return HttpResponse('hello')
	getsession = request.session.get('adminid')=='None'
	if request.session.get('adminid')=='None':
		redirect(admin)
	else:
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			getw =  adminsignup.objects.filter(firstname=username,password=password).order_by('-id')[:1]
			existid = 0
			for i in getw:
				existid = i.id
			
			if existid: 
				request.session['adminid'] = existid
				return redirect(home)
			else:
				error = 'Invalid Username and Password'
				#return HttpResponse(error)
					#return redirect(admin)
					
				return render(request, 'backend/admin.html',{'errors': error})
				
	return render(request, 'backend/admin.html') 

def home(request):
	
	getsession = request.session.get('adminid')
	if getsession:
		getrecord =  adminsignup.objects.get(id=getsession)
		return render(request, 'backend/welcome.html',{'getadta':getrecord}) 
	else:
		return redirect(admin)
	return render(request, 'backend/welcome.html')
	


def services(request):
	getsession = request.session.get('adminid')
	if getsession:
		getrecord =  adminsignup.objects.get(id=getsession)
		error=""
		if request.method == 'POST':
			try:
				#filee = request.files['image_file']
				#filename = secure_filename(file.filename)
				filee = request.FILES.get('image_file')
				servicename = request.POST.get('servicename')
				description = request.POST.get('description') 
				data = Hotelservice(servicename=servicename,description=description,serviceimage=filee)
				data.save()
				error = "Service added successfully"
				return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="Service not added."
				return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error})
		else:
			error=""
			return render(request, 'backend/hotelservices.html',{'getadta':getrecord, 'success':error}) 
		
		
		
		
		#return render(request, 'backend/hotelservices.html',{'getadta':getrecord}) 
	else:
		return redirect(admin)
	#return render(request, 'backend/welcome.html')

############################ add users at backend ########################################

def adduser1(request):
	getsession = request.session.get('adminid')
	getrecord =  adminsignup.objects.get(id=getsession)
	error='';
	if getsession:
		if request.method== 'POST':
			try:
				firstname = request.POST.get('firstname')
				lastname = request.POST.get('lastname')
				username = request.POST.get('username')
				email = request.POST.get('email')
				contact1 = request.POST.get('contact')
				now = datetime.datetime.now()
				#print(request.POST)
			#	return HttpResponse(contact1)
				status = '0'
				data = adduser(firstname=firstname,lastname=lastname,username=username,contactnumber='3213232',dateofjoin=now,status=status,email=email)
				data.save()
				error = "Service added successfully"
				return render(request, 'backend/adduser1.html',{'getadta':getrecord,'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="Service not added."
				return render(request, 'backend/adduser1.html',{ 'getadta':getrecord,'success':error})
		else:
			error=""
			return render(request, 'backend/adduser1.html',{'getadta':getrecord,'success':error}) 
					
				
			
		return render(request, 'backend/adduser1.html') 
	else:
		return redirect(admin)
	#return HttpResponse("dfdfdsfdsf")


def getuser(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getdata1 =  adduser.objects.all()
	return render(request, 'backend/getuser.html',{'getadta':getrecord1,'getrecord':getdata1}) 

def deleteuser(request):
	
		try:
			deluser = request.POST.get('userid')
			#return HttpResponse(delemp)
			#delemp = request.POST.get(id)
			adduser.objects.filter(id=deluser).delete()
			messages.success(request, 'User deleted successfully!')
			return redirect(getuser)
		except KeyError:
				#return HttpResponse(str(e))
				error="Due to error user not deleted."
				return render(request, 'backend/getuser.html',{ 'getadta':getrecord,'success':error})

				
				

def logoutadmin(request):
	#return HttpResponse(request.session['id'])
	try:
		del request.session['adminid']
	#except KeyError as e:
	except KeyError:
		#return HttpResponse(str(e))
		return HttpResponse("You're logged out.")
	return redirect(admin)
	
	
	
#################add employee and get employeeee###########
def addemployee(request):
	getsession = request.session.get('adminid')
	getrecord =  adminsignup.objects.get(id=getsession)
	error='';
	if getsession:
		if request.method== 'POST':
			try:
				employeename = request.POST.get('employeename')
				username = request.POST.get('username')
				email = request.POST.get('email')
				contactnumber = request.POST.get('contact')
				now = datetime.datetime.now()
				#print(request.POST)
				#return HttpResponse(employeename)
				data = employeedetail(employeename=employeename,contactnumber=contactnumber,username=username,dateofjoin=now,email=email)
				data.save()
				error = "New employee added successfully"
				return render(request, 'backend/addnewemployee.html',{'getadta':getrecord,'success':error})
			except KeyError:
				#return HttpResponse(str(e))
				error="New employee not added due to error."
				return render(request, 'backend/addnewemployee.html',{ 'getadta':getrecord,'success':error})
		else:
			error=""
			return render(request, 'backend/addnewemployee.html',{'getadta':getrecord,'success':error}) 
					
				
			
		return render(request, 'backend/addnewemployee.html') 
	else:
		return redirect(admin)
	#return render(request, 'backend/addnewemployee.html')
	
	
def getemployee(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getemployeedetails =  employeedetail.objects.all()
	return render(request, 'backend/getemployee.html',{'getadta':getrecord1,'getemployeedetail':getemployeedetails}) 
	

def deleteemployee(request):
	
		try:
			delemp = request.POST.get('id')
			
			#return HttpResponse(delemp)
			#delemp = request.POST.get(id)
			employeedetail.objects.filter(id=delemp).delete()
			messages.success(request, 'Employee deleted successfully!')
			return redirect(getemployee)
		except KeyError:
				#return HttpResponse(str(e))
				error="Due to error employee not deleted."
				return render(request, 'backend/addnewemployee.html',{ 'getadta':getrecord,'success':error})
	
		
##########################frontend integrationnnnnnnnnnn#######################

##################################holoday page in dutchh.html integration######################################
def woningverhuur(request):
	return render(request, 'woning-verhuur.html')

def fullliteserviceenglish(request):
	if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = fulliteservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					return redirect(holiday)
					
					
			except KeyError:
					return redirect(holiday)
	else:
			 return redirect(holiday)

def fullliteservice(request):
	if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = fulliteservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					return redirect(woningverhuur)
					
					
			except KeyError:
					return redirect(woningverhuur)
	else:
			 return redirect(woningverhuur)
##################################holiday.html for english integration###################################
def holiday(request):
	return render(request, 'en/holiday.html')
	
##################################en.html for english integration###################################
def en(request):
	return render(request, 'en/index.html')


##################################hotel.html integration######################################
def hotel(request):
	return render(request, 'en/hotel.html')
	
	##################################en/pricing.html integration######################################
def pricing(request):
	return render(request, 'en/pricing.html')
	
	

#############singleservice from in pricing for english #####################e
def singleservice1(request):
	if request.method=='POST':
			try:
					name = request.POST.get('name')
					phonenumber = request.POST.get('phonenumber')
					email = request.POST.get('email')
					
			 
					data = singleservice(name=name,email=email,phonenumber=phonenumber) 
					data.save()
					return redirect(pricing)
					
					
			except KeyError:
					return redirect(pricing)
	else:
			 return redirect(pricing)
#############singleservice from in pricing for ductchh #####################e
def singleservicefordutch(request):
	if request.method=='POST':
			try:
					name = request.POST.get('name')
					phonenumber = request.POST.get('phonenumber')
					email = request.POST.get('email')
					data = singleservice(name=name,email=email,phonenumber=phonenumber) 
					data.save()
					return redirect(onzeprijzen)
					
					
			except KeyError:
					return redirect(onzeprijzen)
	else:
			 return redirect(onzeprijzen)
	
	
def help(request):
		
		if request.method=='POST':
			try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					services = request.POST.get('services')
					#now1 = datetime.datetime.now()
					now = datetime.datetime.now()
					#return HttpResponse('hello12')
			 
					data = hotelservice(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,services=services,currentdate=now) 
					data.save()
					return redirect(hotel)
					
					
			except KeyError:
					return redirect(hotel)
					
					
					
		else:
			 return redirect(hotel)
			
			

##################################prize.html integration######################################

def priceperweek(request):
		if request.method== 'POST':
				try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					amount = request.POST.get('amount')
					#now = datetime.datetime.now().strftime('%H:%M')
					verify = '0'
					data = pricingplan(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,amount=amount,verify=verify) 
					data.save()
					mail_subject = 'Activate your blog account.'
					
					message = render_to_string('acc_active_email.html', {
					'user': firstname,
					'domain': 'https://clubfred.herokuapp.com/',
					'uid':data.pk,
					})
					to_email = email
					emails = EmailMessage(
					mail_subject, message, to=[to_email] )
					emails.send()
					messages.success(request, 'Price data is added successfully!')
					return redirect(onzeprijzen)
				except KeyError:
					#return HttpResponse(str(e))
					messages.success(request, 'Price data is not  added successfully!')
					
					return redirect(onzeprijzen)
		else:
			messages.success(request, 'Price data is nott added successfully!')
			return redirect(onzeprijzen)
			
	##################################prize.html for englinshintegration######################################

def priceperweekenglish(request):
		if request.method== 'POST':
				try:
					firstname = request.POST.get('firstname')
					lastname = request.POST.get('lastname')
					email = request.POST.get('email')
					zipcode = request.POST.get('zipcode')
					address = request.POST.get('address')
					mobilenumber = request.POST.get('mobilenumber')
					unit = request.POST.get('unit')
					date = request.POST.get('date')
					amount = request.POST.get('amount')
					now = datetime.datetime.now()
					verify = '0'
					#return HttpResponse(now)
					data = pricingplan(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,amount=amount,verify=verify,currenttime=now) 
					data.save()
					mail_subject = 'Activate your blog account.'
					
					message = render_to_string('acc_active_email.html', {
					'user': firstname,
					'domain': 'https://clubfred.herokuapp.com/',
					'uid':data.pk,
					})
					to_email = email
					emails = EmailMessage(
					mail_subject, message, to=[to_email] )
					emails.send()
					messages.success(request, 'Price data is added successfully!')
					return redirect(pricing)
				except KeyError:
					#return HttpResponse(str(e))
					messages.success(request, 'Price data is not  added successfully!')
					
					return redirect(pricing)
		else:
			messages.success(request, 'Price data is nott added successfully!')
			return redirect(pricing)

def abc(request):

	date_time_newer = datetime.datetime.now()
	user = pricingplan.objects.get(id=31)
	cureentdatetime = datetime.datetime.strptime(user.currenttime,'%Y-%m-%d %H:%M:%S.%f')
	date_time_difference = (date_time_newer-cureentdatetime).total_seconds()/60
	return HttpResponse(date_time_difference)
	
	
############activate confirmation#####################
			
def activate(request, uidb64):
	try:
		uid = uidb64
		user = pricingplan.objects.get(pk=uid)
		date_time_newer = datetime.datetime.now()
		user = pricingplan.objects.get(id=31)
		cureentdatetime = datetime.datetime.strptime(user.currenttime,'%Y-%m-%d %H:%M:%S.%f')
		date_time_difference = (date_time_newer-cureentdatetime).total_seconds()/60
		return HttpResponse(date_time_difference)
		user.verify = 1
		user.save()
		return HttpResponse('Thank you for your  confirmation.')
	except(TypeError, ValueError, OverflowError, pricingplan.DoesNotExist):
			user = None
			user.verify = 1
			user.save()
			#login(request, user)
			# return redirect('home')
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
			
def pricingplans(request):
		getsession = request.session.get('adminid')
		getrecord1 =  adminsignup.objects.get(id=getsession)
		getpricing =  pricingplan.objects.filter(verify=1)
		return render(request, 'backend/pricingplan.html',{'getadta':getrecord1,'getpricingdetail':getpricing}) 
		
def airbnb(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getdata1 =  fulliteservice.objects.all()
	return render(request, 'backend/airbnb.html',{'getadta':getrecord1,'getrecord':getdata1}) 

def hotels(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getdata1 =  hotelservice.objects.all()
	return render(request, 'backend/hotelservice.html',{'getadta':getrecord1,'getrecord':getdata1}) 

def getsingleservices(request):
	getsession = request.session.get('adminid')
	getrecord1 =  adminsignup.objects.get(id=getsession)
	getdata1 =  singleservice.objects.all()
	return render(request, 'backend/singleservice.html',{'getadta':getrecord1,'getrecord':getdata1}) 
	