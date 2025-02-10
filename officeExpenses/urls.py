from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # path('hotel-bookings/', views.HotelListView.as_view(), name='hotel-booking-list'),
    # path('hotel-bookings/', views.HotelListView.as_view(), name='hotel-booking-detail'),

]