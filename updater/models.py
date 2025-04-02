from django.db import models


class Product(models.Model):
    """
    Model representing a product.
    """
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    provider = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.sku
    