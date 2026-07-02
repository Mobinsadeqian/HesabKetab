from django.contrib import admin
from .models import Payment, Invoice

admin.site.register(Payment)
admin.site.register(Invoice)