from django.urls import path
from . import views

app_name = 'hotels'

urlpatterns = [
    path('', views.HotelBookingListView.as_view(), name='list-bookings'),
    # path('<int:pk>', views.HotelBookingDetailView.as_view(), name='detail-booking'),
    path('create/', views.HotelBookingCreateView.as_view(), name='create-booking'),
    path('<int:pk>/update', views.HotelBookingUpdateView.as_view(), name='update-booking'),
    path('<int:pk>/delete', views.HotelBookingDeleteView.as_view(), name='delete-booking'),
]