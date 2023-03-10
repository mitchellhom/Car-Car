from django.urls import path
from .views import (
    api_list_technicians,
    api_list_appointments,
    api_show_appointment,
)

urlpatterns = [
    path('technicians/', api_list_technicians, name="api_list_technicians"),
    path('appointments/', api_list_appointments, name="api_list_appointments"),
    path('appointments/<str:vin_num>/', api_list_appointments, name="api_list_appt_by_vin"),
    path('appointments/detail/<int:pk>/', api_show_appointment, name="api_show_appointment"),
]
