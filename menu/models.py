from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    

    class MPTTMeta:
        order_insertion_by = ['name']
    class Meta:
        verbose_name_plural = u"Categories"
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'), blank=True, null=True)
    category = TreeForeignKey('Category', null=True, blank=True, db_index=True)

    def __str__(self):
        return self.name
