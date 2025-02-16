from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import login
from hotelBookings.models import HotelBooking
from carHires.models import CarHire
from officeExpenses.models import OfficeExpense
from django.db.models import Sum


# Create your views here.
class HomepageView(generic.TemplateView):
    template_name = "index.html"

class SignupView(generic.CreateView):
    template_name = "form_template.html"
    form_class = forms.CustomUserCreationForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create New Account'
        context['form_title'] = 'Create an account'
        context['form_subtitle'] = 'Please enter details to create your account'
        context['form_submit_text'] = 'Create account'
        return context
    
    def get_success_url(self):
        return reverse('dashboard')

class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'
    # model = HotelBooking

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hour = datetime.now().hour

        match hour:
            case h if 5 <= h < 12:
                greeting = 'Good morning'
            case h if 12 <= h < 18:
                greeting = 'Good afternoon'
            case h if 18 <= h < 22:
                greeting = 'Good evening'
            case _:
                greeting = 'Good night'

        context['greeting'] = greeting

        context['total_carhire_cost'] = CarHire.objects.aggregate(total=Sum('trip_cost'))['total'] or 0
        context['total_office_expense_cost'] = OfficeExpense.objects.aggregate(total=Sum('cost'))['total'] or 0

        hotel_cost = 0
        hotel_bookings = HotelBooking.objects.all()        
        for hotel_booking in hotel_bookings:
            date_difference = hotel_booking.check_out - hotel_booking.check_in
            date_difference_in_days = date_difference.days
            hotel_booking_cost = hotel_booking.hotel_name.cost_per_night * date_difference_in_days
            hotel_cost += hotel_booking_cost

        context['total_hotel_booking_cost'] = hotel_cost
        context['total_cost_to_organisation'] = context['total_carhire_cost'] + context['total_office_expense_cost'] + context['total_hotel_booking_cost']

        return context