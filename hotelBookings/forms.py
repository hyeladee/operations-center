from django import forms
from .models import HotelBooking, Hotel

class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = '__all__'