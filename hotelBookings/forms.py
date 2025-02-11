from django import forms
from .models import HotelBooking, Hotel

class HotelBookingModelForm(forms.ModelForm):
    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )
    check_out = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
        required=False
    )
    
    class Meta:
        model = HotelBooking
        fields = '__all__'