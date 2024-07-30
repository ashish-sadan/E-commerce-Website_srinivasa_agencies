from django.urls import path , include
from . import views
urlpatterns = [
    
    path("", views.Registerpage, name = "registerpage"),
    path("register/", views.UserRegister, name = "register"),
    path("loginPage/", views.LoginPage,name = "loginpage"),
    path("LoginUser/", views.LoginUser, name = "login"),
    path("rose/", views.rose, name = "roses"),
    path("new/", views.Home, name = "home"),
    path("Cookies/", views.Cookies, name = "cookies"),
    path("Popcorn/", views.Popcorn, name = "popcorn"),
    path("Rotary/", views.Rotary, name = "rotary"),
    path("Wafers/", views.Wafers, name = "wafers"),
    path("Papad/", views.Papad, name = "papad"),
    path("Checkout/", views.Checkout, name = "checkout"),
    path("Store/", views.Store, name = "store"),
    path("cart/", views.Cart, name = "cart"),
    path("update_item/", views.updateItem, name = "update_item"),

]
