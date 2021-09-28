from django.urls import path
from . import views

urlpatterns = [
    path('home',views.index, name='index'),
    path('register',views.register, name='register'),
    path('display',views.display, name='display')
]