from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = self.product.new_price * self.quantity

    def __str__(self):
        return str(self.quantity) + " of " + self.product.name

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = 0
        for item in self.items.all():
            self.total_price += item.total_price

    def __str__(self):
        if self.ordered_date:
            return self.user.username + " ordered " + str(self.ordered_date.date()) + "  " + str(self.ordered_date.time())
        else:
            return self.user.username
