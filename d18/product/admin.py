from django.contrib import admin

# Register your models here.
from product.models import *
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)