from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


# Create your views here.
class HotelBookingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'hotelBookings/hotel_booking_list.html'
    context_object_name = 'hotel_bookings'
    model = models.HotelBooking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for index, hotel_booking in enumerate(context['hotel_bookings'], start=1):
            hotel_booking.serial = index
            date_difference = hotel_booking.check_out - hotel_booking.check_in
            hotel_booking.days = date_difference.days
            hotel_booking.cost = hotel_booking.hotel_name.cost_per_night * hotel_booking.days
        return context

class HotelBookingCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'form_template.html'
    form_class = forms.HotelBookingModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'New Hotel Booking'
        context['form_title'] = 'Create Hotel Booking'
        context['form_subtitle'] = 'Enter a new hotel booking record'
        context['form_submit_text'] = 'Create'
        return context

    def get_success_url(self) -> str:
        return reverse('hotels:list-bookings')

class HotelBookingUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'form_template.html'
    form_class = forms.HotelBookingModelForm
    context_object_name = 'booking_record'
    model = models.HotelBooking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Hotel Record'
        context['form_title'] = 'Hotel booking for ' + str(self.object.guest_name)
        context['form_subtitle'] = (
            'Update record for ' + str(self.object.guest_name) +
            ' at ' + str(self.object.hotel_name) +
            ' on ' + str(self.object.check_in)
        )
        context['form_submit_text'] = 'Update'
        context['update_url'] = True
        context['hotel'] = True

        return context

    def get_success_url(self) -> str:
        return reverse('hotels:list-bookings')

class HotelBookingDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "form_template.html"
    model = models.HotelBooking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Hotel Record'
        context['form_title'] = 'Delete booking for ' + str(self.object.guest_name)
        context['form_subtitle'] = ('Are you sure you want to delete the booking for ' + str(self.object.guest_name) +
            ' at ' + str(self.object.hotel_name) +
            ' on ' + str(self.object.check_in)
        )
        context['form_submit_text'] = 'Confirm Delete'
        context['delete_url'] = True
        context['hotel'] = True
        return context
    
    def get_success_url(self) -> str:
        return reverse('hotels:list-bookings')