from django.urls import path
from . import views
urlpatterns = [
    path('expenses/', views.show_expenses),
    path('add_expense/', views.add_expense, name='add_new_expense'),
    path('delete_expense/<int:expense_id>', views.delete_expense, name='delete_expense'),
    path('edit_expense/<int:expense_id>', views.edit_expense, name='edit_expense'),
    path('unit_factors/<str:unit_id>', views.unit_factors, name='unit_factors'),
    path('admin_unit_factors/<str:unit_id>', views.admin_unit_factors, name='admin_unit_factors'),
    path('submit_payment/<str:factor_id>', views.submit_payment, name='submit_payment'),
    path('upload_receipt/<str:factor_id>', views.upload_receipt, name='upload_receipt'),
]