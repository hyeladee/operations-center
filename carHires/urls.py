from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarHireListView.as_view(), name='carhire-list'),
    path('<int:pk>', views.CarHireDetailView.as_view(), name='carhire-detail'),
    path('create', views.CarHireCreateView.as_view(), name='carhire-create'),
    path('update/<int:pk>', views.CarHireUpdateView.as_view(), name='carhire-update'),
    path('delete/<int:pk>', views.CarHireDeleteView.as_view(), name='carhire-delete'),
]