import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import loginfo
from datetime import datetime

# Create your views here.
def login_user(request):
    # u = User.objects.get(username = 'John')
    # # u.get_username("1")
    # u.set_password('12345')
    # u.save()
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
            u = User.objects.get(username = request.POST['username'])
            # u.get_username("1")
            u.set_password(request.POST['password'])
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

def logingo(request):
    if request.method == 'POST':
        uname = request.user
        uemail = request.POST['username']
        uid = request.user.id
        user = User.objects.get(username = uname)
        user.first_name = request.POST['fname']
        user.last_name =request.POST['lname']
        user.save()
        log = loginfo()
        result = loginfo.objects.filter(user_key = uname).exists()
        print(result)
        # print(datetime.now())
        dt = str(datetime.now())
        dt = dt.replace(' ', '')
        dt = dt.replace('-', '')
        dt = dt.replace(':', '')
        dt = dt.split('.')
        if result:
            print('pass')
            loginfo.objects.filter(user_key = uname).update(
                address = request.POST['add'],
                city = request.POST['city'],
                unique_code = int(dt[0])
            )
        else:
            print('fail')
            log = loginfo()
            log.email = uemail
            log.uname = uname
            log.address = request.POST['add']
            log.city = request.POST['city']
            log.user_key = uname
            log.unique_code = int(dt[0])
            log.save()

        return render(request, 'home.html')
    
def reveal_secret(request):
    uname = request.user.id
    data = loginfo.objects.filter(user_key_id = uname)
    return render(request, 'home.html', {'data': data})

def data_reveal(request, id):
    result = loginfo.objects.filter(unique_code = id).all()
    print(result[0])
    a = str(result[0]).split(' ')
    print(a[5])
    # for i in result:
    #     print(i)
    # a = str(result).split(' ')
    return JsonResponse(
        {
            'email': a[0],
            'username': a[1],
            'address': a[2],
            'city': a[3],
            'user_key': a[4],
            'secret_key': a[5],
        })