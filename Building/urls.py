from django.urls import path
from .models import BuildingExpense, BuildManager, Unit
from . import views

urlpatterns = [
    path('signup/',views.register_new_manager, name='signup_manager'),
    path('login_manager', views.login_manager, name="login_manager"),
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('logout/', views.logout_user, name='logout_user'),
    path('add_new_unit', views.add_new_unit, name='add_new_unit'),
    path('delete_unit/<int:unit_id>', views.delete_unit, name='delete_unit'),
    path('edit_unit/<int:unit_id>', views.edit_unit, name='edit_unit'),
    path('building_page', views.building_page, name='building_page'),
    path('edit_manager_info/<str:manager_id>', views.edit_manager_info, name='edit_manager_info'),
    path('update_manager_info/<str:manager_id>', views.update_manager_info, name='update_manager_info'),



]