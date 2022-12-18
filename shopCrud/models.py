from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, default="")
    price = models.FloatField(
        validators=[MinValueValidator(0.0)], default=1
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0.0)], default=0
    )
    image = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name