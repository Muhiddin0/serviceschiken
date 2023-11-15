from django.urls import path
from .views import stopVet, export_excel

app_name = 'vet'
urlpatterns = [
    path('stop/<int:pk>', stopVet, name='stop'),
    path('excel/', export_excel, name='excel')
]