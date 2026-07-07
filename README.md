<div align="center">

# 🧾 حساب‌کتاب | HesabKetab

**سامانه هوشمند مدیریت مالی ساختمان — ثبت هزینه، تقسیم خودکار شارژ و پیگیری فاکتور واحدها**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0.6-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-در%20حال%20توسعه-yellow?style=flat-square)]()

[🔴 مشاهده دمو زنده](https://hesabketab.pythonanywhere.com/) · [گزارش باگ](https://github.com/Mobinsadeqian/HesabKetab/issues)

</div>

---

## درباره پروژه

مدیریت شارژ و هزینه‌های مشترک ساختمان معمولاً روی اکسل، دفترچه کاغذی یا گروه تلگرام انجام می‌شود؛ روشی که پیگیری بدهی هر واحد و شفافیت هزینه‌ها را سخت می‌کند. **حساب‌کتاب** یک وب‌اپلیکیشن جنگویی است که این فرآیند را برای مدیر ساختمان و ساکنین واحدها دیجیتال و شفاف می‌کند: مدیر یک هزینه را ثبت می‌کند، سیستم آن را بین همه واحدها تقسیم و برای هرکدام فاکتور جداگانه صادر می‌کند، و ساکن با یک کد اختصاصی (بدون نیاز به ثبت‌نام) صورت‌حساب خودش را می‌بیند و رسید واریزی آپلود می‌کند.

این پروژه به‌صورت شخصی و برای یادگیری عمیق‌تر جنگو در یک سناریوی واقعی ساخته شده و در حال حاضر روی [PythonAnywhere](https://hesabketab.pythonanywhere.com/) دیپلوی شده است.

## ✨ امکانات

### برای مدیر ساختمان
- ثبت‌نام و ورود با تولید خودکار کد ساختمان (`build_id`) و شناسه مدیر
- تعریف، ویرایش و حذف واحدهای ساختمان
- ثبت هزینه مشترک و **تقسیم خودکار مبلغ به‌صورت مساوی بین تمام واحدها**
- صدور خودکار فاکتور جداگانه برای هر واحد به ازای هر هزینه، با شناسهٔ فاکتور یکتا
- مشاهدهٔ وضعیت پرداخت فاکتورهای هر واحد و ثبت تأیید پرداخت
- ویرایش اطلاعات حساب مدیر (نام، شمارهٔ تماس، شمارهٔ کارت جهت واریز، رمز عبور)
- نمایش تاریخ ثبت هزینه‌ها به تقویم شمسی (با `jdatetime`)

### برای ساکنین واحدها
- دسترسی به صورت‌حساب واحد صرفاً با وارد کردن کد ساختمان — بدون نیاز به ثبت‌نام
- مشاهدهٔ فهرست فاکتورهای صادرشده برای واحد و وضعیت هرکدام (پرداخت‌شده / پرداخت‌نشده)
- آپلود تصویر رسید واریزی برای هر فاکتور

## 🧱 معماری پروژه

پروژه به‌صورت دو اپ جنگو مجزا و decouple‌شده طراحی شده:

```
hesabketab/
├── Building/          # مدیریت ساختمان، مدیر (کاربر سفارشی) و واحدها
│   ├── models.py      # BuildManager (AbstractUser), Unit, BuildingExpense
│   └── views.py
├── Finance/            # لایهٔ مالی: فاکتور و پرداخت
│   ├── models.py      # Invoice, Payment
│   └── views.py
├── hesabketab/         # تنظیمات و URLConf اصلی پروژه
├── templates/          # قالب‌های HTML (Tailwind + فونت وزیرمتن، راست‌به‌چپ)
└── Scripts/
```

- **مدل کاربر سفارشی:** `BuildManager` جایگزین مدل پیش‌فرض جنگو شده (`AUTH_USER_MODEL`) تا مدیر ساختمان مستقیماً کاربر احراز هویت‌شده باشد.
- **رابطهٔ Building ↔ Finance:** مدل‌های `Invoice` و `Payment` در اپ `Finance` به `Unit` و `BuildingExpense` در اپ `Building` ارجاع می‌دهند؛ این جداسازی، منطق ساختمان را از منطق مالی مستقل نگه می‌دارد.
- هر `Unit` یک `unit_id` یکتا دارد که مبنای دسترسی بدون لاگین ساکنین است، و فیلد `telegram_chat_id` برای اطلاع‌رسانی آینده از طریق تلگرام از قبل در مدل پیش‌بینی شده.

## 🛠️ تکنولوژی‌های استفاده‌شده

| لایه | تکنولوژی |
|---|---|
| بک‌اند | Python, Django 6.0.6 |
| پایگاه داده | SQLite |
| تاریخ شمسی | jdatetime, jalali_core |
| مدیریت تصویر | Pillow (آپلود رسید پرداخت) |
| فرانت‌اند | Tailwind CSS (CDN), فونت Vazirmatn, طراحی راست‌به‌چپ |
| دیپلوی | PythonAnywhere |

## 🚀 نصب و اجرای پروژه به‌صورت لوکال

```bash
# ۱. کلون پروژه
git clone https://github.com/Mobinsadeqian/HesabKetab.git
cd HesabKetab

# ۲. ساخت و فعال‌سازی محیط مجازی
python -m venv venv
source venv/bin/activate      # ویندوز: venv\Scripts\activate

# ۳. نصب پیش‌نیازها
pip install -r requirements.txt

# ۴. اجرای مایگریشن‌ها
python manage.py migrate

# ۵. اجرای سرور توسعه
python manage.py runserver
```

سپس پروژه روی آدرس `http://127.0.0.1:8000/` در دسترس است.

## 🗺️ نقشه راه

- [ ] ساخت REST API با Django REST Framework برای اتصال اپلیکیشن موبایل
- [ ] فعال‌سازی اطلاع‌رسانی پرداخت از طریق ربات تلگرام (بر پایهٔ فیلد `telegram_chat_id`)
- [ ] تکمیل چرخهٔ تأیید پرداخت با کد پیگیری بانکی (مدل `Payment`)
- [ ] نوشتن تست‌های خودکار (unit / integration)
- [ ] پنل گزارش‌گیری مالی برای مدیر (خروجی و نمودار هزینه‌ها)

## 👨‍💻 دربارهٔ سازنده

این پروژه توسط **مبین**، توسعه‌دهندهٔ جونیور بک‌اند (Python / Django)، به‌عنوان یک پروژهٔ واقعی برای تمرین طراحی و ساخت اپلیکیشن‌های چندکاربره ساخته شده است.

- گیت‌هاب: [Mobinsadeqian](https://github.com/Mobinsadeqian)
- تلگرام: [@Mobinsadeqian](https://t.me/Mobinsadeqian)
- ایمیل: mobinsadeghian2003@gmail.com

اگر پیشنهاد، باگ یا ایده‌ای برای بهتر شدن پروژه دارید، از طریق [Issues](https://github.com/Mobinsadeqian/HesabKetab/issues) یا شبکه‌های بالا خوشحال می‌شوم بشنوم.
