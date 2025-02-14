from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms


# Create your views here.
class OfficeExpenseListView(LoginRequiredMixin, generic.ListView):
    template_name = 'officeExpenses/office_expense_list.html'
    context_object_name = 'office_expenses'
    model = models.OfficeExpense

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for index, office_expense in enumerate(context['office_expenses'], start=1):
            office_expense.serial = index
        return context

class OfficeExpenseCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'form_template.html'
    form_class = forms.OfficeExpenseModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'New Office Expense'
        context['form_title'] = 'Create Office Expense'
        context['form_subtitle'] = 'Enter a new office expense record'
        context['form_submit_text'] = 'Create'
        return context

    def get_success_url(self) -> str:
        return reverse('office-expenses:list-office-expenses')

class OfficeExpenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'form_template.html'
    form_class = forms.OfficeExpenseModelForm
    context_object_name = 'office_expenses'
    model = models.OfficeExpense

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Office Expense Record'
        context['form_title'] = 'Office expense record for ' + str(self.object.description)
        context['form_subtitle'] = (
            'Update record for ' + str(self.object.description) +
            ' by ' + str(self.object.vendor.name) +
            ' on ' + str(self.object.date)
        )
        context['form_submit_text'] = 'Update'
        context['update_url'] = True
        context['office_expense'] = True
        return context

    def get_success_url(self) -> str:
        return reverse('office-expenses:list-office-expenses')
    

class OfficeExpenseDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "form_template.html"
    model = models.OfficeExpense

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Office Expense Record'
        context['form_title'] = 'Delete booking for ' + str(self.object.description)
        context['form_subtitle'] = ('Are you sure you want to delete the record for ' + str(self.object.description) +
            ' by ' + str(self.object.vendor.name) +
            ' on ' + str(self.object.date)
        )
        context['form_submit_text'] = 'Confirm Delete'
        context['delete_url'] = True
        context['office_expense'] = True
        return context
    
    def get_success_url(self) -> str:
        return reverse('office-expenses:list-office-expenses')
    