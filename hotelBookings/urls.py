from django.urls import path
from . import views

urlpatterns = [
    path('', views.HotelBookingListView.as_view(), name='hotel-booking-list'),
    # path('<int:pk>', views.HotelBookingDetailView.as_view(), name='hotel-booking-detail'),
    # path('create/', views.HotelBookingCreateView.as_view(), name='hotel-booking-create'),
    # path('<int:pk>/update', views.HotelBookingUpdateView.as_view(), name='hotel-booking-update'),
    # path('<int:pk>/delete', views.HotelBookingDeleteView.as_view(), name='hotel-booking-delete'),
]