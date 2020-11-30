from django.db import models

from core.models import BaseModel, INRField, TAXField, MARGINField


# Create your models here.
class Pricing(BaseModel):

    PRICING_TYPE_INWARD = 'INWARD'
    PRICING_TYPE_OUTWARD = 'OUTWARD'

    PRICING_TYPE_CHOICES = (
        (PRICING_TYPE_INWARD, 'In-Ward'),
        (PRICING_TYPE_OUTWARD, 'Out-Ward'),
    )

    type        = models.CharField(max_length=50, choices=PRICING_TYPE_CHOICES, default=PRICING_TYPE_INWARD)
    amount      = INRField(default=0, help_text='Amount in INR')
    margin      = MARGINField(default=0, null=True, blank=True)
    cgst        = TAXField(default=0, null=True, blank=True)
    sgst        = TAXField(default=0, null=True, blank=True)
    cess        = TAXField(default=0, null=True, blank=True)
    other_tax   = TAXField(default=0, null=True, blank=True)
    over_head   = INRField(default=0, null=True, blank=True)


    @property
    def total_amount(self):
        cgst        = self.cgst * self.amount
        sgst        = self.sgst * self.amount
        cess        = self.cess * self.amount
        other_tax   = self.other_tax * self.amount
        return self.amount + cgst + sgst + cess + other_tax + self.over_head