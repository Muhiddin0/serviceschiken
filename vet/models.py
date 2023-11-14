from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class VetUsers(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class VetClient(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    humidity = models.CharField(max_length=250)
    temperature = models.CharField(max_length=250)
    sickness = models.CharField(max_length=250)
    diagnose = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images_uploaded', null=True)

    def __str__(self) -> str:
        return self.name

# Jo`jaxonani rasm va videoga olib yuboring