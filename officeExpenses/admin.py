from django.contrib import admin
from .models import OfficeExpense, ExpenseType, Vendor

# Register your models here.
admin.site.register(Vendor)
admin.site.register(ExpenseType)
admin.site.register(OfficeExpense)