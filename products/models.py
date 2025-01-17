from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)
    description = models.TextField(default=now)
    created_at = models.DateTimeField(default=now)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default=now)
    
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.0)
    imageUrl = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name

