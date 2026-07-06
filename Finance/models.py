from django.db import models
from Building.models import Unit, BuildingExpense

class Invoice(models.Model):

    STATUS_CHOICES = [
        ('paid', 'پرداخت شده'),
        ('unpaid', 'پرداخت نشده'),
    ]

    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='invoices', verbose_name='واحد')
    expense = models.ForeignKey(BuildingExpense, on_delete=models.SET_NULL, null=True, blank=True, related_name='invoices', verbose_name='بابت هزینه')
    amount = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='مبلغ سهم هر واحد (تومان)')
    status = models.CharField(choices=STATUS_CHOICES,max_length=10, default='unpaid', verbose_name='وضعیت پرداخت')
    due_time = models.DateTimeField(verbose_name='مهلت پرداخت', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ صدور فاکتور')
    factor_id = models.CharField(max_length=34, null=True, blank=True, unique=True, verbose_name='آیدی فاکتور')
    factor_image = models.ImageField(upload_to='factor_image/', null=True, blank=True, verbose_name='تصویر رسید پرداخت')

    def __str__(self):
        return f"فاکتور واحد {self.unit.unit_number} -{self.unit.unit_name} - {self.amount:,} تومان ({self.get_status_display()})"
    
    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتورها"

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار تایید مدیر'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده')
    ]
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='payments', verbose_name='واحد')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments', verbose_name='برای فاکتور')
    amount_paid = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='مبلغ واریزی (تومان)')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ پرداخت')
    tracking_code = models.CharField(max_length=100, unique=True, verbose_name='کد پیگیری بانکی')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='pending', verbose_name='وضعیت رسید')

    def __str__(self):
        return f"رسید واحد {self.unit.unit_number} - {self.amount_paid:,} تومان ({self.get_status_display()})"
    
    class Meta:
        verbose_name = 'پرداختی'
        verbose_name_plural = 'پرداختی‌ها'
