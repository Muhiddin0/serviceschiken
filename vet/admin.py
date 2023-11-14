from django.contrib import admin
from .models import VetUsers, VetClient

# Register your models here.
admin.site.register(VetUsers)
admin.site.register(VetClient)