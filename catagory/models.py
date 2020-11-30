from django.db import models

from core.models import BaseModel

# Create your models here.
class Catagory(BaseModel):
    name            = models.CharField(max_length=500)
    description     = models.TextField(blank=True, null=True)
    image           = models.ImageField(blank=True, null=True)