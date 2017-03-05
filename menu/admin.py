from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import Category, Product

class MenuMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Category, MenuMPTTModelAdmin)
admin.site.register(Product, admin.ModelAdmin)


# Register your models here.
