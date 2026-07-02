from django.shortcuts import render, redirect, get_object_or_404
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