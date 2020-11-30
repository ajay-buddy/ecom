from django.db import models

from core.models import BaseModel
from pricing.models import Pricing
from category.models import Category
from inventory.models import Inventory

# Create your models here.

class Product(BaseModel):

    PRODUCT_LIFE_MONTH = 'MONTH'
    PRODUCT_LIFE_WEEK = 'WEEK'
    PRODUCT_LIFE_DAYS = 'DAYS'
    PRODUCT_LIFE_YEAR = 'YEAR'

    PRODUCT_LIFE_CHOICE = (
        (PRODUCT_LIFE_DAYS, 'days'),
        (PRODUCT_LIFE_MONTH, 'month'),
        (PRODUCT_LIFE_WEEK, 'week'),
        (PRODUCT_LIFE_YEAR, 'year'),
    )

    name                = models.CharField(max_length=500)
    description         = models.TextField(blank=True, null=True)
    image               = models.ImageField(blank=True, null=True)
    SKU                 = models.CharField(max_length=200, null=True, blank=True)
    barcode             = models.CharField(max_length=200, blank=True, null=True)
    # pricing           = models.ForeignKey(Pricing, null=True, blank=True, on_delete=models.CASCADE)
    # inventory         = models.ForeignKey(Inventory, null=True, blank=True, on_delete=models.CASCADE)
    category            = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    product_life        = models.IntegerField(blank=True, null=True)
    product_life_type   = models.CharField(max_length=20, choices=PRODUCT_LIFE_CHOICE, blank=True, null=True)
    