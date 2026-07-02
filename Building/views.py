from django.shortcuts import render, redirect
from .models import BuildManager
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register_new_manager(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        card_number = request.POST.get('card_number')
        user = BuildManager.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, phone_number=phone_number, card_number=card_number)
        return redirect('login_manager')
    return render(request, 'building/signup.html')

def login_manager(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manager_dashboard')
        else:
            return render(request, 'building/login_manager.html')
    return render(request, 'building/login_manager.html')

@login_required
def manager_dashboard(request):
    return render(request, 'building/manager_dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('home_page')