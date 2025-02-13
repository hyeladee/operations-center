from django import forms
from .models import CarHire

class CarHireModelForm(forms.ModelForm):
    trip_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )

    class Meta:
        model = CarHire
        fields = '__all__'