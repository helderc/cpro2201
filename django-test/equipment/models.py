from django.db import models

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=60)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
