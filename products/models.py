from django.db import models
from categories.models import Category
from django.core.exceptions import ValidationError

from django.urls import reverse

# Create your models here.
class Product(models.Model):
    AVAILABILITY_CHOICES = [('in', 'In Stock'), ('no', 'Non-Available')]
    EXTRA_CHOICES = [
        ('sale', 'Sale'),
        ('new', 'New'),
        ('hot', 'Hot'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    related_product = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    characteristics = models.TextField()
    description = models.TextField(blank=True)
    old_price = models.PositiveIntegerField(null=True, blank=True)
    new_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(null=True, default=10)
    main_image = models.ImageField(upload_to='products/images/', default='No Image')
    product_extra = models.CharField(max_length=5, choices=EXTRA_CHOICES, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/images/', default='No Image')

    def __str__(self):
        image_name = self.image.url.split('/')[-1]
        return image_name

    def clean(self):
        product_images = ProductImage.objects.filter(product=self.product)
        if product_images.count() >= 3:
            raise ValidationError(f'More than 4 images per product! Please delete some of the images for {self.product.name} uploaded before.')
