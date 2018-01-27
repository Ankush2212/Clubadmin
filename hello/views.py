import requests


from django.contrib.sessions.models import Session
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import adduser 
from .models import adminsignup 
from .models import employeedetail 
import datetime


# Create your views here.
def index(request):
    #return HttpResponse('Hefdd gfdgdf llo fddcccx xczfddvd x dddrom Python!')
	# services = Hotelservice.objects.all()
	 return render(request, 'index.html')

def getdata(request):
	 getdata =  Contact.objects.all()
	# getdata =  Contact.objects.order_by('first_name')
	 return render(request, 'getdata.html',{'getrecord':getdata})

def user_details(request,userid):
	 getparticularrecord =  Contact.objects.get(id=userid)
	 #return HttpResponse(getparticularrecord.first_name)
	 return render(request, 'getresponse.html',{'getresponse':getparticularrecord})
 

def updateuserrecord(request):
	firstname = request.POST.get('firstname')
	lastname = request.POST.get('lastname')
	email = request.POST.get('email')
	description = request.POST.get('description')
	userid = request.POST.get('userid')
	to_update = Contact.objects.filter(id=userid).update(first_name=firstname,last_name=lastname,email=email,description=description)
	return redirect(getdata)

def deleteuser(request,userid):
	Contact.objects.filter(id=userid).delete()
	return redirect(getdata)
	
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
				#date = request.POST.get('date')
				now = datetime.datetime.now()
				#print(request.POST)
				#return HttpResponse(now)
				status = '0'
				data = adduser(firstname=firstname,lastname=lastname,username=username,dateofjoin=now,status=status,email=email)
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
			getsession = request.session.get('adminid')
			getrecord1 =  adminsignup.objects.get(id=getsession)
			getemployeedetails =  employeedetail.objects.all()
			successer="Employee deleted successfully."
			return render(request, 'backend/getemployee.html',{'getadta':getrecord1,'getemployeedetail':getemployeedetails,'success':successer})
		except KeyError:
				#return HttpResponse(str(e))
				error="Due to error employee not deleted."
				return render(request, 'backend/addnewemployee.html',{ 'getadta':getrecord,'success':error})
	
		
	#return HttpResponse("You're logged out.")
	#Contact.objects.filter(id=userid).delete()
	#return redirect(getdata)