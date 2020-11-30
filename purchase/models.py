from django.db import models

from core.models import BaseModel, QuantityField
from vendor.models import Vendor
# Create your models here.
class Purchase(BaseModel):
    vendor = models.ForeignKey(Vendor, null=True, blank=True)