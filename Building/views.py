from django.shortcuts import render, redirect, get_object_or_404
from .models import BuildManager, BuildingExpense, Unit
from Finance.models import Payment, Invoice
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
import random
from django.contrib import messages

def register_new_manager(request):
    if request.method == "POST":
        build_id = random.randint(1234567, 1234567891115)
        manager_id = random.randint(1234567891, 123456789112)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        card_number = request.POST.get('card_number')
        user = BuildManager.objects.create_user(first_name=first_name,manager_id=manager_id, build_id=build_id, last_name=last_name, username=username, password=password, phone_number=phone_number, card_number=card_number)
        return redirect('login_manager')
    return render(request, 'building/signup.html')

def login_manager(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("manager_dashboard")
        else:
            messages.error(
                request, "نام کاربری یا رمز عبور اشتباه است."
            )
            return render(request, "building/login_manager.html")

    return render(request, "building/login_manager.html")

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
        unit_id = random.randint(12345667, 9548383282)
        Unit.objects.create(unit_name=unit_name, unit_number=unit_number, phone_number=unit_phone_number, manager=current_user, unit_id=unit_id)
        messages.success(request, 'واحد جدید با موفقیت اضافه شد')
        return redirect('manager_dashboard')
    return render(request, 'building/add_new_unit.html')

def delete_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id, manager=request.user)
    unit.delete()
    messages.success(request, 'عملیات حذف با موفقیت انجام شد')
    return redirect('manager_dashboard')

def edit_unit(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id, manager=request.user)
    if request.method == 'POST':
        unit.unit_name = request.POST.get('unit_name')
        unit.unit_number = request.POST.get('unit_number')
        unit.unit_phone_number = request.POST.get('unit_phonenumber')
        unit.save()
        messages.success(request, 'عملیات آپدیت اطلاعات واحد با موفقیت انجام شد')
        return redirect('manager_dashboard')
    context = {
            'unit' : unit
        }
    return render(request, 'building/edit_unit.html', context)


def building_page(request):
    if request.method == "GET":
        build_id = request.GET.get('build_id')
        build = get_object_or_404(BuildManager, build_id=build_id)
        units = build.units.all()
        expenses = build.expenses.all().order_by('-id')

        context = {
            'build_id' : build_id,
            'build' : build,
            'units': units,
            'expenses': expenses
        }
        return render(request, 'building/building_page.html',context)
    

def edit_manager_info(request, manager_id):
    manager = get_object_or_404(BuildManager, manager_id=manager_id)
    context = {
        'manager' : manager
    }
    return render(request, 'building/edit_manager_info.html', context)

def update_manager_info(request, manager_id):
    manager = get_object_or_404(BuildManager, manager_id=manager_id)
    if request.method == "POST":
        manager.first_name = request.POST.get('manager_first_name')
        manager.last_name = request.POST.get('manager_last_name')
        manager.username = request.POST.get('manager_username')
        manager.phone_number = request.POST.get('manager_phone_number')
        manager.card_number = request.POST.get('manager_card_number')

        new_password = request.POST.get('manager_password')
        if new_password and new_password.strip() != "":
            manager.set_password(new_password)
        manager.save()
        login(request, manager)
        messages.success(request, "اطلاعات مدیریتی شما با موفقیت بروزرسانی شد.")
        return redirect('manager_dashboard')
    context = {'manager': manager}
    return render(request, 'building/edit_manager_info.html', context)