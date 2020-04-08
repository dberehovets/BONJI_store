from django.contrib import admin
from products.models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):

    search_fields = ['name']

    list_filter = ['category', 'product_extra']

    list_display = ['name', 'old_price', 'new_price', 'category', 'quantity', 'main_image']

    list_editable = ['quantity']

class ProductImageAdmin(admin.ModelAdmin):

    search_fields = ['image']

    list_display = ['__str__', 'product', 'image']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
