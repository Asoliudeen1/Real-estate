from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if len(password) < 8:
                messages.error(request, 'Password must not less than 8 chracters')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.error(request, 'That email is being used')
                 return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registered successfully')
                return redirect('login')
        else:
            messages.error(request,'Password don not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def Dashboard(request):
    return render(request, 'accounts/dashboard.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credetials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    messages.success(request, 'you are now logout ')
    return redirect('home')
