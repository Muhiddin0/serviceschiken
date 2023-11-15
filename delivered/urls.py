from django.urls import path
from .views import stopDelivred, export_excel

app_name = 'delivred'
urlpatterns = [
    path('stop/<int:pk>', stopDelivred, name='stop'),
    path('excel/', export_excel, name='excel')
]