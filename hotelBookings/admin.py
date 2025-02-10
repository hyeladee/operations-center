from django.contrib import admin
from .models import HotelBooking, Hotel

# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelBooking)
