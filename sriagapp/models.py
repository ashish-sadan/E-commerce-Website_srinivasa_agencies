from django.db import models
from django.contrib.auth.models import User

from django.shortcuts import render , redirect
from django.http import JsonResponse
import json

from .models import *


# Create your models here.
#class Student(models.Model):
#    Firstname = models.CharField(max_length=50)
#    Lastname = models.CharField(max_length=50)
#    Email = modls.EmailField(max_length=50)
#   Contact = models.BigIntegerField()

class Users(models.Model):
	Firstname = models.CharField(max_length=50)
	Lastname = models.CharField(max_length=50)
	Email = models.EmailField(max_length=50)
	Contact = models.CharField(max_length=50)
	Password = models.CharField(max_length=50)

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
		
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping
	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total
	
	
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank= True, null = True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null = True)
	quantity = models.IntegerField(default=0, null=True , blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

