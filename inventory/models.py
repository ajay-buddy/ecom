from django.db import models

from core.models import BaseModel, QuantityField
from vendor.models import Vendor
from customer.models import Customer
from product.models import Product
from pricing.models import Pricing
# Create your models here.
class Inventory(BaseModel):
    product         = models.ForeignKey(Product)
    quantity        = QuantityField(default=0, blank=True, null=True)

class InventoryBatch(BaseModel):
    vendor          = models.ForeignKey(Vendor)
    product         = models.ForeignKey(Product)
    price           = models.ForeignKey(Pricing)
    quantity        = QuantityField(default=0)
    expiry_date     = models.DateField(blank=True, null=True)

class InventoryAudit(BaseModel):
    product         = models.ForeignKey(Product)
    previous        = QuantityField()
    added           = QuantityField()
    reduced         = QuantityField()
    available       = QuantityField()
    is_adjustment   = models.BooleanField(default=True)
    vendor          = models.ForeignKey(Vendor, blank=True, null=True)
    customer        = models.ForeignKey(Customer, blank=True, null=True)
