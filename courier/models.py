import os
from django.db import models
from twilio.rest import Client


# Create your models here.

class Container(models.Model):
	CT_STATUS = (
		
		('Loaded','Loaded'),
		('Arrived','Arrived'),
		
	)
	container_no = models.CharField(max_length=200, null=True)
	cont_status =models.CharField(max_length=200,null=True,choices=CT_STATUS,blank=True)

	


	def __str__(self):
		return self.container_no
	

class Customer(models.Model):
	STATUS = (
		('Collected','Collected'),
		('Loaded','Loaded'),
		('Arrived','Arrived'),
		('Delivered','Delivered')
	)

	name = models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=200,null=True)
	pieces = models.CharField(max_length=200,null=True)
	container = models.ForeignKey(Container,null=True,on_delete=models.CASCADE,blank=True)	
	status = models.CharField(max_length=200,null=True,choices=STATUS,blank=True,default='Collected')
	
	def __str__(self):
		return self.name


	