from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Invoice, Payment
from Building.models import BuildingExpense, BuildManager, Unit
import random

def show_expenses(request):
    return HttpResponse(request, 'hello from financial page')


def add_expense(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST.get('title_expnese')
        amount = request.POST.get('amount_expnese')
        units = current_user.units.all()
        unit_numbers = len(units)
        if unit_numbers == 0:
            return render(request, 'finance/add_new_expense.html', {
                'error': 'شما هنوز هیچ واحدی ثبت نکرده‌اید! ابتدا واحدها را بسازید.'
        })
        unit_amount = int(amount) / unit_numbers #مبلغ هر واحد
        expense = BuildingExpense.objects.create(title=title, total_amount=amount, manager=current_user)
        for unit in units:
            factor_id = random.randint(959589393,39040059585)
            Invoice.objects.create(
                unit=unit, 
                expense=expense, 
                amount=unit_amount,
                factor_id=factor_id
            )
        return redirect('manager_dashboard')
    return render(request, 'finance/add_new_expense.html')

def delete_expense(request, expense_id):
    expense = get_object_or_404(BuildingExpense, id=expense_id, manager=request.user)
    expense.delete()
    return redirect('manager_dashboard')

def edit_expense(request, expense_id):
    expense = get_object_or_404(BuildingExpense, id=expense_id, manager=request.user)
    if request.method == "POST":
        expense.title = request.POST.get('expense_title')
        expense.total_amount = request.POST.get('expense_amount')
        expense.save()
        return redirect('manager_dashboard')
    context = {
        'expense' : expense
    }
    return render(request, 'finance/edit_expense.html', context)

def unit_factors(request, unit_id):
    unit = get_object_or_404(Unit, unit_id=unit_id)
    factors = Invoice.objects.filter(unit=unit)
    context = {
        'factors': factors
    }
    return render(request, 'finance/unit_factors.html', context)

def admin_unit_factors(request, unit_id):
    unit = get_object_or_404(Unit, unit_id=unit_id)
    factors = Invoice.objects.filter(unit=unit)
    context = {
        'factors': factors
    }
    return render(request, 'finance/admin_unit_factors.html', context)

def submit_payment(request, factor_id):
    factor = get_object_or_404(Invoice, factor_id=factor_id)
    factor.status = 'paid'
    factor.save()
    return redirect('manager_dashboard')