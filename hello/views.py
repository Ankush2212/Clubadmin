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

from .models import adduser 
from .models import adminsignup 
from .models import employeedetail 
from .models import pricingplan 
import datetime
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
	
		
	#return HttpResponse("You're logged out.")
	#Contact.objects.filter(id=userid).delete()
	#return redirect(getdata)
	# def send_email(to_list, subject, message, sender="Aircourts <noreply@aircourts.com>"):
    # msg = EmailMessage(subject, message, sender, to_list)
    # msg.content_subtype = "html"  # Main content is now text/html
    # return msg.send()
	
##########################frontend integrationnnnnnnnnnn#######################
def abc(request):
	# name="kalpana"
	# sender="kalpana@codenomad.net"
	# subject="testing"
	# #to="test@gmail.com"
	# message="<a href='#'>click here</a>"
	# msg = EmailMessage(subject, message, sender)
	# msg.content_subtype = "html"  # Main content is now text/html
	# return msg.send()
	sender="kalpana@codenomad.net"
	subject = 'Some subject'
	from_email = sender
	message = 'This is my test message'
	recipient_list = [sender]
	html_message = '<a href="https://www.programcreek.com/">This is my HTML test</a>'


	send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
	return  HttpResponse('firstname')
##pricing page form per week55/70###

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
					verify = '0'
					#print(request.POST)
					#return HttpResponse(firstname)
					#sender="kalpana@codenomad.net"
					# subject = 'Please verify you booking'
					# from_email = email
					# message = 'Here is a activitation link please click on that and verify your booking.'
					# recipient_list = [email]
					# html_message = '<a href="{% url 'verify' email %}">Verify your booking</a>'


					# send_mail(subject, message, from_email , recipient_list, fail_silently=False, html_message=html_message)
					
					mail_subject = 'Activate your blog account.'
					
					message = render_to_string('acc_active_email.html', {
					'user': firstname,
					'domain': 'https://clubfred.herokuapp.com/',
					'uid':urlsafe_base64_encode(str(firstname)),
					})
					to_email = email
					emails = EmailMessage(
					mail_subject, message, to=[to_email] )
					emails.send()
					#return HttpResponse('Please confirm your email address to complete the registration')
					
					
					
					
					
					data = pricingplan(firstname=firstname,lastname=lastname,zipcode=zipcode,address=address,email=email,mobilenumber=mobilenumber,unit=unit,datetimee=date,amount=amount,verify=verify) 
					data.save()
					messages.success(request, 'Price data is added successfully!')
					return redirect(onzeprijzen)
				except KeyError:
					#return HttpResponse(str(e))
					messages.success(request, 'Price data is not  added successfully!')
					
					return redirect(onzeprijzen)
		else:
			messages.success(request, 'Price data is nott added successfully!')
			return redirect(onzeprijzen)
	
def activate(request, uidb64):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		return HttpResponse(str(uid))
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
		if user is not None and account_activation_token.check_token(user):
			user.is_active = True
			user.save()
			login(request, user)
			# return redirect('home')
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
		else:
			return HttpResponse('Activation link is invalid!')