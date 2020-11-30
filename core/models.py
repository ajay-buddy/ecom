from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class INRField(models.DecimalField):
    def __init__(self, **kwargs):
        kwargs['max_digits'] = 12
        kwargs['decimal_places'] = 2
        super().__init__(**kwargs)

class TAXField(models.DecimalField):
    def __init__(self, **kwargs):
        kwargs['max_digits'] = 3
        kwargs['decimal_places'] = 2
        super().__init__(**kwargs)

class MARGINField(models.DecimalField):
    def __init__(self, **kwargs):
        kwargs['max_digits'] = 3
        kwargs['decimal_places'] = 2
        super().__init__(**kwargs)

class QuantityField(models.DecimalField):
    def __init__(self, **kwargs):
        kwargs['max_digits'] = 3
        kwargs['decimal_places'] = 2
        super().__init__(**kwargs)

class BaseModel(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)
    updated_by      = models.ForeignKey(User, related_name='updated_by_user')
    created_by      = models.ForeignKey(User, related_name='created_by_user')
    is_active       = models.BooleanField(default=False)