from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('trackerApp.urls')),
    path('carhires/', include('carHires.urls')),
    path('hotel-bookings/', include('hotelBookings.urls')),
    path('office-expenses/', include('officeExpenses.urls')),
]
