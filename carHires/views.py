from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


# Create your views here.
class CarHireListView(LoginRequiredMixin, generic.ListView):
    template_name = 'carHires/carhire_list.html'
    context_object_name = 'carhires'
    model = models.CarHire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for index, carhire in enumerate(context['carhires'], start=1):
            carhire.serial = index
        return context

class CarHireCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'form_template.html'
    form_class = forms.CarHireModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'New Car Hire'
        context['form_title'] = 'Create Car Hire'
        context['form_subtitle'] = 'Enter a new car hire record'
        context['form_submit_text'] = 'Create'
        return context

    def get_success_url(self) -> str:
        return reverse('carhires:list-carhires')

class CarHireUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'form_template.html'
    form_class = forms.CarHireModelForm
    context_object_name = 'carhires'
    model = models.CarHire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Car Hire Record'
        context['form_title'] = 'Car hire record for ' + str(self.object.passenger_name)
        context['form_subtitle'] = (
            'Update record for ' + str(self.object.passenger_name) +
            ' by ' + str(self.object.vendor.name) +
            ' on ' + str(self.object.trip_date)
        )
        context['form_submit_text'] = 'Update'
        context['update_url'] = True
        context['carhire'] = True
        return context

    def get_success_url(self) -> str:
        return reverse('carhires:list-carhires')

class CarHireDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "form_template.html"
    model = models.CarHire

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Car Hire Record'
        context['form_title'] = 'Delete booking for ' + str(self.object.passenger_name)
        context['form_subtitle'] = ('Are you sure you want to delete the record for ' + str(self.object.passenger_name) +
            ' by ' + str(self.object.vendor.name) +
            ' on ' + str(self.object.trip_date)
        )
        context['form_submit_text'] = 'Confirm Delete'
        context['delete_url'] = True
        context['carhire'] = True
        return context
    
    def get_success_url(self) -> str:
        return reverse('carhires:list-carhires')