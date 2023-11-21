from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')
    # return HttpResponse("Home")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone =request.POST.get('phone')
        desc =request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message is send succesfully")  # ignored

    return render(request, 'contact.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, "login succesfully")
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect")
            return render(request, 'login.html')
    else :
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')