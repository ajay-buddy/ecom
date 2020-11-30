from django.db import models

from core.models import BaseModel, QuantityField
from company.models import Company
from product.models import Product
# Create your models here.

class Store(BaseModel):
    name        = models.CharField(max_length=255)
    company     = models.ForeignKey(Company)
    address     = models.TextField(blank=True, null=True)
    landline1   = models.CharField(max_length=255, blank=True, null=True)
    landline2   = models.CharField(max_length=255, blank=True, null=True)
    phone2      = models.CharField(max_length=255, blank=True, null=True)
    phone2      = models.CharField(max_length=255, blank=True, null=True)
    fax         = models.CharField(max_length=255, blank=True, null=True)

class Shelf(BaseModel):
    store       = models.ForeignKey(Store)
    capacity    = QuantityField(default=0)
    barcode     = models.CharField(max_length=200, blank=True, null=True)
    product     = models.ForeignKey(Product, blank=True, null=True)
    quantity    = QuantityField(default=0)
    is_leased   = models.BooleanField(default=False)

class ShelfAudit(BaseModel):
    shelf                   = models.ForeignKey(Shelf)
    previous_product        = models.ForeignKey(Product)
    previous_quantity       = QuantityField(default=0)
    new_product             = models.ForeignKey(Product)
    new_quantity            = QuantityField(default=0)
    is_leased               = models.BooleanField(default=False)

