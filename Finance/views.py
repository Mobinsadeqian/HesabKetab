from django.shortcuts import render, redirect
from django.http import HttpResponse


def show_expenses(request):
    return HttpResponse(request, 'hello from financial page')
