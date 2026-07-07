from django.db import models
from django.contrib.auth.models import AbstractUser
import jdatetime

class BuildManager(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره همراه مدیر")
    card_number = models.CharField(max_length=16, blank=True, null=True, verbose_name="شماره کارت جهت واریز شارژ")
    build_id = models.CharField(max_length=20, unique=True,blank=True, null=True, verbose_name='کد ساختمان')
    manager_id = models.CharField(max_length=34, unique=True, blank=True, null=True, verbose_name='آیدی مدیر')

    
    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name} - {self.manager_id}"
        return self.username
    
class Unit(models.Model):
    manager = models.ForeignKey(BuildManager, on_delete=models.CASCADE, related_name='units', verbose_name='مدیر ساختمان')
    unit_name = models.CharField(max_length=40, blank=False, null=False, verbose_name='نام مالک واحد')
    unit_number = models.PositiveIntegerField(verbose_name='شماره واحد')
    phone_number = models.CharField(max_length=11, verbose_name='شماره همراه مالک')
    telegram_chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='آیدی تلگرام مالک')
    unit_id = models.CharField(max_length=40, unique=True, blank=True, null=True, verbose_name='آیدی واحد')

    def __str__(self):
        return f"واحد {self.unit_number} - {self.unit_name}"
    
    class Meta:
        verbose_name = 'واحد'
        verbose_name_plural = 'واحدها'

class BuildingExpense(models.Model):
    manager = models.ForeignKey(BuildManager, on_delete=models.CASCADE, related_name='expenses', verbose_name='مدیر ساختمان')
    title = models.CharField(max_length=255, verbose_name='عنوان هزینه')
    total_amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='مبلغ کل (تومان)')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    @property
    def jalali_date(self):
        if self.date_created:
            # 🌟 روش استاندارد و بدون خطا برای تبدیل به شمسی با فرمت دلخواه
            date_shamsi = jdatetime.date.fromgregorian(
                date=self.date_created
            )
            return date_shamsi.strftime("%Y/%m/%d")
        return ""

    def __str__(self):
        return f"{self.title} - {self.total_amount:,} تومان"
    
    class Meta:
        verbose_name = 'هزینه ساختمان'
        verbose_name_plural = 'هزینه‌های ساختمان'

