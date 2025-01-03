from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=now)
    created_at = models.DateTimeField(default=now)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

