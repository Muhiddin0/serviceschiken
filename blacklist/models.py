from django.db import models

# Create your models here.
class Blacklist(models.Model):
    user_id = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.user_id