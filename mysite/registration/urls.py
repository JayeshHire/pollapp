from django.urls import path
from . import views


#use isinstance to check if an object belongs to a class 
urlpatterns = [
    path('login/', views.login_form, name= "login"),
    path('auth/',views.login_view, name='auth')
]