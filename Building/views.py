from django.shortcuts import render, redirect, get_object_or_404
from .models import BuildManager, BuildingExpense, Unit
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
    current_manager = request.user
    my_units = Unit.objects.filter(manager=current_manager)
    expenses = BuildingExpense.objects.filter(manager=current_manager)


    context = {
        'units' : my_units,
        'expenses' : expenses,
        'user': current_manager
    }
    return render(request, 'building/manager_dashboard.html', context)

def logout_user(request):
    logout(request)
    return redirect('home_page')

def add_new_unit(request):
    if request.method == "POST":
        unit_name = request.POST.get('unit_name')
        unit_number = request.POST.get('unit_number')
        unit_phone_number = request.POST.get('unit_phone_number')
        current_user = request.user
        Unit.objects.create(unit_name=unit_name, unit_number=unit_number, phone_number=unit_phone_number, manager=current_user)
        return redirect('manager_dashboard')
    return render(request, 'building/add_new_unit.html')

def delete_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id, manager=request.user)
    unit.delete()
    return redirect('manager_dashboard')

def edit_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id, manager=request.user)
    if request.method == 'POST':
        unit.unit_name = request.POST.get('unit_name')
        unit.unit_number = request.POST.get('unit_number')
        unit.unit_phone_number = request.POST.get('unit_phonenumber')
        unit.save()
        return redirect('manager_dashboard')
    context = {
            'unit' : unit
        }
    return render(request, 'building/edit_unit.html', context)