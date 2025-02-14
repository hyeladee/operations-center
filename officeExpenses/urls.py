from django.urls import path
from . import views

app_name = 'office-expenses'

urlpatterns = [
    path('', views.OfficeExpenseListView.as_view(), name='list-office-expenses'),
    # path('<int:pk>', views.OfficeExpenseDetailView.as_view(), name='detail-office-expense'),
    path('create', views.OfficeExpenseCreateView.as_view(), name='create-office-expense'),
    path('update/<int:pk>', views.OfficeExpenseUpdateView.as_view(), name='update-office-expense'),
    path('delete/<int:pk>', views.OfficeExpenseDeleteView.as_view(), name='delete-office-expense'),
]