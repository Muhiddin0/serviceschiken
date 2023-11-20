from django.db import models

import datetime

class DeliverUsers(models.Model):
    user_id = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Delivered(models.Model):
    
    ISO_date = "2021-12-18"
    default_date = datetime.date.fromisoformat(ISO_date)

    delivered = models.ForeignKey(DeliverUsers, on_delete=models.Case)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    img = models.TextField()
    comment_img = models.TextField()
    comment = models.CharField(max_length=400)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name