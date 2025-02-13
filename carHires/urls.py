from django.urls import path
from . import views

app_name = 'carhires'

urlpatterns = [
    path('', views.CarHireListView.as_view(), name='list-carhires'),
    # path('<int:pk>', views.CarHireDetailView.as_view(), name='detail-carhire'),
    path('create', views.CarHireCreateView.as_view(), name='create-carhire'),
    path('update/<int:pk>', views.CarHireUpdateView.as_view(), name='update-carhire'),
    path('delete/<int:pk>', views.CarHireDeleteView.as_view(), name='delete-carhire'),
]