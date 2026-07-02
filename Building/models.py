from django.db import models
from django.contrib.auth.models import AbstractUser

class BuildManager(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره همراه مدیر")
    card_number = models.CharField(max_length=16, blank=True, null=True, verbose_name="شماره کارت جهت واریز شارژ")

    
    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
class Unit(models.Model):
    manager = models.ForeignKey(BuildManager, on_delete=models.CASCADE, related_name='units', verbose_name='مدیر ساختمان')
    unit_name = models.CharField(max_length=40, unique=True, blank=False, null=False, verbose_name='نام مالک واحد')
    unit_number = models.PositiveIntegerField(unique=True, verbose_name='شماره واحد')
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه مالک')
    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='آیدی تلگرام مالک')

    def __str__(self):
        return f"واحد {self.unit_number} - {self.resident_name}"
    
    class Meta:
        verbose_name = 'واحد'
        verbose_name_plural = 'واحدها'

class BuildingExpense(models.Model):
    manager = models.ForeignKey(BuildManager, on_delete=models.CASCADE, related_name='expenses', verbose_name='مدیر ساختمان')
    title = models.CharField(max_length=255, verbose_name='عنوان هزینه')
    total_amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='مبلغ کل (تومان)')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f"{self.title} - {self.total_amount:,} تومان"
    
    class Meta:
        verbose_name = 'هزینه ساختمان'
        verbose_name_plural = 'هزینه‌های ساختمان'

