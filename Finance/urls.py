from django.urls import path
from . import views
urlpatterns = [
    path('expenses', views.show_expenses)
]