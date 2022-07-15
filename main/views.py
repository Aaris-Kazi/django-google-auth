from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        print(user)
        if user is not None:
            login(request, user)
            # messages.add_message(request, messages.SUCCESS, 'Login successful')
            return render(request, 'home.html')
        else:
            messages.add_message(request, messages.ERROR, 'Login invalid please check username or passowrd')
            return render(request,'login.html')
    else:
        messages.add_message(request, messages.ERROR, '')
        return render(request,'login.html')
        
def register(request):
    if request.method == 'POST':
        try:
            u = User()
            u.username = request.POST['username']
            u.email = request.POST['email']
            u.password = request.POST['password']
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
        except Exception:
            messages.add_message(request, messages.ERROR, 'A issue occur during registering')
        return render(request,'register.html')
    else:
        messages.add_message(request, messages.ERROR, '')
        # auth_user
    return render(request,'register.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def index(request):
    return render(request, 'home.html')

def qr_maker(request):
    user = User.objects.get()
    return render(request, 'home.html')
    
