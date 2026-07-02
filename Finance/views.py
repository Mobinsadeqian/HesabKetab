from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invoice, Payment
from Building.models import BuildingExpense, BuildManager, Unit

def show_expenses(request):
    return HttpResponse(request, 'hello from financial page')


def add_expense(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST.get('title_expnese')
        amount = request.POST.get('amount_expnese')
        expense = BuildingExpense.objects.create(title=title, total_amount=amount, manager=current_user)
        return redirect('manager_dashboard')
    return render(request, 'finance/add_new_expense.html')