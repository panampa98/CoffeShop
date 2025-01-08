from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=255, verbose_name='Name')
    description = models.TextField(max_length=255, verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    available = models.BooleanField(default=True, verbose_name='Available')
    image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Image')

    def __str__(self):
        return self.name