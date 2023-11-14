from django.urls import path
from .views import index, xabr_yuborish

app_name = 'index'
urlpatterns = [
    path('', index, name='index'),
]