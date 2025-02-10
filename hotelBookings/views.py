from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HotelBooking
from .forms import HotelBookingForm


# Create your views here.
class HotelBookingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'hotelBookings/hotel_booking_list.html'
    context_object_name = 'hotel_bookings'
    model = HotelBooking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for index, hotel_booking in enumerate(context['hotel_bookings'], start=1):
            hotel_booking.serial = index
            date_difference = hotel_booking.check_out - hotel_booking.check_in
            hotel_booking.days = date_difference.days
            hotel_booking.cost = hotel_booking.hotel_name.cost_per_night * hotel_booking.days

        return context

