from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HotelBooking
from .forms import HotelBookingForm

# Create your views here.
class HotelBookingListView(LoginRequiredMixin, generic.ListView):
    template_name = "list_template.html"
    context_object_name = 'hotel_bookings'
    model = HotelBooking
    
