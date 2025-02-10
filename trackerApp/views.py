from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomepageView(generic.TemplateView):
    template_name = "index.html"

class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"

# TODO signup page
# class SignupView(generic.TemplateView):
#     template_name = "signup.html"