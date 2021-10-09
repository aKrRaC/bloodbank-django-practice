from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('home',views.home, name = 'home'),
    path('add-donor',views.register, name = 'register'),
    path('display',views.display, name = 'display')
]