from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import login

# Create your views here.
class HomepageView(generic.TemplateView):
    template_name = "index.html"

class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"
    context_object_name = 'dashboard'
    

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
        return context

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