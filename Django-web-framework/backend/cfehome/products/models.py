from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=99.99)