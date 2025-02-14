from django import forms
from .models import OfficeExpense

class OfficeExpenseModelForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )

    class Meta:
        model = OfficeExpense
        fields = '__all__'