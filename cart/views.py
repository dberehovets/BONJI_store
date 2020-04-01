from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from products.models import Product
from django.utils import timezone
from django.contrib import messages
from django.views.generic import DetailView

class CartDetail(DetailView):
    model = Cart

def add_to_cart(request, product_pk, qty):
    product = get_object_or_404(Product, pk=product_pk)
    if product.quantity >= int(qty):
        cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user = request.user,
        ordered=False)

        cart_qs = Cart.objects.filter(user=request.user, ordered=False)

        if cart_qs.exists():
            cart = cart_qs[0]

            if cart.items.filter(product__pk=product.pk, ordered=False).exists():
                cart_item.quantity += 1
                cart_item.save()
            else:
                cart.items.add(cart_item)
        else:
            cart = Cart.objects.create(user=request.user)
            cart.items.add(cart_item)
        product.quantity -= 1
        product.save()
    else:
        messages.add_message(request, messages.WARNING, "Shortage of products in stock", fail_silently=True)
    return redirect('products:product_detail', pk=product_pk)


def remove_from_cart(request, item_pk):
    cart_item = CartItem.objects.get(pk=item_pk)
    cart_item.product.quantity += cart_item.quantity
    cart_item.product.save()
    cart_pk = cart_item.cart.pk
    cart_item.remove()
    return redirect('cart:cart_detail', pk=cart_pk)
