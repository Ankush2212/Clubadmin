from django.db import models

# Create your models here.
#class Greeting(models.Model):
    #when = models.DateTimeField('date created', auto_now_add=True)
	
	

class Contact(models.Model):
   
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	description = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now= True)

class adminsignup(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	email = models.EmailField(blank=True)
	
class adduser(models.Model):
	firstname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	dateofjoin = models.CharField(max_length=250)
	status = models.IntegerField()
	email = models.EmailField(blank=True)
class addemployee(models.Model):
	employeename = models.CharField(max_length=250)
	username = models.CharField(max_length=250)
	dateofjoin = models.CharField(max_length=250)
	contact = models.CharField(max_length=250)
	status = models.IntegerField()
	email = models.EmailField(blank=True)

