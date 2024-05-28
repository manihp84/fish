from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('service/', views.service,name='service'),
    path('create/', views.create,name='create'),
    path('read/', views.read,name='read'),
    path('update/<int:id>', views.edit,name='edit'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('change_path/, <str:new_path>/',views.change_path,name='change_path'),
    
]