from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import emp
from.forms import empForm
# Create your views here.
def index(request):
    return render(request,'waterapp/index.html')
def about(request):
    return render(request,'waterapp/about.html')
def contact(request):
    return render(request,'waterapp/contact.html')
def login(request):
    return render(request,'waterapp/login.html')
def signup(request):
    return render(request,'waterapp/signup.html')
def service(request):
    return render(request,'waterapp/service.html')
def change_path(request, new_path):
    return redirect(new_path)

def create(request):
    if request.method == 'POST':
        fm = empForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse("success")
    else:
        fm = empForm()
    return render(request,'waterapp/create.html',{'fm':fm})

def read(request):
    data = emp.objects.all()
    return render(request,'waterapp/read.html',{'data':data})

def edit(request,id):
    dataget = emp.objects.get(id=id)
    data = emp.objects.all()
    fm = empForm(instance=dataget)
    if request.method == 'POST':
        fm = empForm(request.POST,instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('read')
    return render(request,'waterapp/edit.html',{'fm':fm,'data':data})

def delete(request,id):
    dataget = emp.objects.get(id=id)
    dataget.delete()
    return redirect('read')

   