from django.contrib import admin
from cart.models import Cart, CartItem

## CART MODELS CAN BE ADDED IF NEEDED.
## FOR NOW ADMIN DOESN'T NEED TO HAVE CART MODELS

admin.site.register(Cart)
admin.site.register(CartItem)
