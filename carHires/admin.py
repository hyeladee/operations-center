from django.contrib import admin
from .models import CarHire, Vendor, Location

# Register your models here.
admin.site.register(Vendor)
admin.site.register(CarHire)
admin.site.register(Location)
