from django.db import models
from products.models import Product

class TelegramCustomer(models.Model):
    telegram_id = models.CharField(max_length=32, unique=True)
    username = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        if self.username:
            return f"@{self.username}"
        else:
            return str(self.telegram_id)


class TelegramCart(models.Model):
    user = models.ForeignKey(TelegramCustomer, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(null=True)
    ordered = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = 0
        self.product_quantity = 0
        for item in self.items.all():
            self.total_price += item.total_price
            self.product_quantity += item.quantity

    def __str__(self):
        user_name = str(self.user.telegram_id) + " " + self.user.first_name + " " + self.user.last_name
        if self.ordered_date:
            return user_name + " ordered " + str(self.ordered_date.date()) + "  " + str(self.ordered_date.time())
        else:
            return user_name


class TelegramCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(TelegramCart, related_name='items', on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total_price = self.product.new_price * self.quantity

    def __str__(self):
        return str(self.quantity) + " of " + self.product.name
