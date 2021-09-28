from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup',views.signup_page, name = 'signup_page'),
    path('login',views.login_page, name = 'login_page'),
    path('home',views.home, name = 'home_page'),
    path('register',views.register_page, name= 'register_page'),
    path('display',views.display, name = 'display_page'),
    path('signup_user',views.signup, name = "signup_user"),
    path('login_user',views.login, name = "login_user"),
    path('register_user',views.register, name = "register_user")
]