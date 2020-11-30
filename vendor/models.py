from django.db import models

from core.models import BaseModel
# Create your models here.

class Vendor(BaseModel):
    name        = models.CharField(max_length=255)
    address     = models.TextField(blank=True, null=True)
    landline1   = models.CharField(max_length=255, blank=True, null=True)
    landline2   = models.CharField(max_length=255, blank=True, null=True)
    phone2      = models.CharField(max_length=255, blank=True, null=True)
    phone2      = models.CharField(max_length=255, blank=True, null=True)
    fax         = models.CharField(max_length=255, blank=True, null=True)