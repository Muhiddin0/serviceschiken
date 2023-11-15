from django.urls import path
from .views import index, delivers, vets

app_name = 'index'
urlpatterns = [
    path('', index, name='home'),
    path('delivers/', delivers, name='delivres'),
    path('vets/', vets, name='vets'),
]