from django.urls import path
from . import views
urlpatterns = [
    path('expenses/', views.show_expenses),
    path('add_expense/', views.add_expense, name='add_new_expense'),
    path('delete_expense/<int:expense_id>', views.delete_expense, name='delete_expense'),
]