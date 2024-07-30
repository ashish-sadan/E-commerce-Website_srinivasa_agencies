from django.contrib import admin
from .models import *

# admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)