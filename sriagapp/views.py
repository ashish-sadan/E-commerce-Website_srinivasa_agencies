from django.shortcuts import render , redirect
from django.http import JsonResponse
import json

from .models import *

def Registerpage(request):
    return render(request, "app/register.html")

def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contant']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        users = Users.objects.filter(Email=email)

        if users:
            message = "User already exist"
            return render(request, "app/login.html",{'msg':message})
        
        else:
            if password == cpassword:
                newuser = Users.objects.create(Firstname=fname, Lastname=lname, Email = email,
                                              Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "password and Confirm Password Doesnot Match"
                return render(request,"app/register.html",{'msg': message})
            
def LoginPage(request):
    return render(request, "app/login.html")
            
def Home(request):
    return render(request, "app/new.html")

def rose(request):
    return render(request, "app/roses.html")

def rose(request):
    return render(request, "app/.html")

def rose(request):
    return render(request, "app/roses.html")

def Papad(request):
    return render(request, "app/papad.html")

def Popcorn(request):
    return render(request, "app/popcorn.html")

def Rotary(request):
    return render(request, "app/rotary.html")

def Wafers(request):
    return render(request, "app/wafers.html")

def Cookies(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 , 'shipping':False}
        cartItems = order['get_cart_total']
    products = Product.objects.all()
    context = {'products':products , 'cartItems': cartItems}
    return render(request, "app/addtocart_cookies.html" , context)

def Checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0 , 'shipping':False}
        cartItems = order['get_cart_total']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, "app/checkout.html" , context)

def Store(request):
    return render(request, "app/store.html")

def Cart(request):
    return render(request, "app/cart.html")

 
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        users = Users.objects.get(Email=email)

        if users:
            if users.Password == password:
                request.session['Firstname'] = users.Firstname
                request.session['Lastname'] = users.Lastname
                request.session['Email'] = users.Email
                return render(request, "app/new.html")
            else:
                message = "password does not match"
                return render(request, "app/login.html", {'msg':message})

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
