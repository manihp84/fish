from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .decorators import login_required 
from .models import emp
from.forms import empForm
from .forms import signupmodel, loginform
from django.contrib.auth.hashers import check_password  # Import password checking utility
from django.contrib.auth import login as auth_login, get_user_model
from .models import signup
from django.contrib import messages 
# Create your views here.

def index(request):
    return render(request,'waterapp/index.html')
@login_required
def about(request):
    return render(request,'waterapp/about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate the data (simple example, add more checks as needed)
        if name and email and message:
            emp.objects.create(name=name, email=email, message=message)
            return HttpResponse('success')  # Define a success URL or view
    return render(request, 'waterapp/contact.html')
    # return render(request,'waterapp/contact.html')
def login(request):
    return render(request,'waterapp/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = signupmodel(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password==confirm_password:
                form.save()    
                return HttpResponse('success')  # Define a success URL or view
            else:
                return HttpResponse('password not match')
    else:
        form = signupmodel()
    return render(request, 'waterapp/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        f = loginform(request.POST)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
            print(username)
            print(password)
            try:
                user = signup.objects.get(username=username)
                if user.password == password:
                    print(user)
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    f.save()
                    return redirect('/')   # Redirect to a success URL or view
                else:
                    return HttpResponse('Invalid credentials')
            except signup.DoesNotExist:
                return HttpResponse('Invalid credentials')
    else:
        f = loginform()
        if 'next' in request.GET:
            messages.warning(request, "You need to be logged in to access this page.")
    return render(request, 'waterapp/login.html', {"f": f})


def service(request):
    return render(request,'waterapp/service.html')
def change_path(request, new_path):
    return redirect(new_path)

def pinki(request):
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

def emp1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate the data (simple example, add more checks as needed)
        if name and email and message:
            emp.objects.create(name=name, email=email, message=message)
            return HttpResponse('success')  # Define a success URL or view
    return render(request, 'waterapp/contact.html')
   