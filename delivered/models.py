from django.db import models


class DeliverUsers(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Delivered(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    img = models.ImageField(upload_to='chicken_uploaded', null=True)
    comment = models.ImageField(upload_to="chicken_home")

    def __str__(self) -> str:
        return self.name
# Create your models here.
