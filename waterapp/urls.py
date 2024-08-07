from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('submit/', views.emp1, name='my_form'),
    path('login/', views.login,name='login'),
    path('signup_view/', views.signup_view ,name='signup_view'),
    path('logout/', views.logout_view, name='logout'),
    path('service/', views.service,name='service'),
    path('create/', views.pinki,name='create'),
    path('read/', views.read,name='read'),
    path('update/<int:id>', views.edit,name='edit'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('change_path/, <str:new_path>/',views.change_path,name='change_path'),
    
]