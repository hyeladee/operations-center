from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")  
        # field_classes = {"username": UsernameField}

        
