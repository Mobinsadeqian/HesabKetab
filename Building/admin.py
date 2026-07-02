from django.contrib import admin
from .models import BuildingExpense, BuildManager, Unit

admin.site.register(BuildingExpense)
admin.site.register(BuildManager)
admin.site.register(Unit)
