from django.db import models
from django.core.validators import FileExtensionValidator

import datetime

# Create your models here.
class VetUsers(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class VetClient(models.Model):
        
    ISO_date = "2021-12-18"
    default_date= datetime.date.fromisoformat(ISO_date)

    vet = models.ForeignKey(VetUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    humidity = models.CharField(max_length=250)
    temperature = models.CharField(max_length=250)
    sickness = models.CharField(max_length=250)
    diagnose = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images_uploaded', null=True)
    create_at = models.DateField(default=default_date)

    def __str__(self) -> str:
        return self.name