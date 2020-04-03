from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from products.models import Product
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, FormView
from django.contrib.auth.decorators import login_required
from cart.forms import CheckOutForm
from django.http import HttpResponseRedirect

class CartDetail(DetailView):
    model = Cart


class CheckOut(SuccessMessageMixin, FormView):
    template_name = 'cart/checkout.html'
    form_class = CheckOutForm
    success_url = '/'
    success_message = "Thank you! Our manager will contact you shortly!"

    def form_valid(self, form):
        ## sending telegram message. Under development!
        cart = Cart.objects.get(user=self.request.user, ordered=False)
        for item in cart.items.all():
            item.ordered = True
            item.save()
        cart.ordered = True
        cart.ordered_date = timezone.now()
        cart.save()
        return super().form_valid(form)

@login_required
def add_to_cart(request, product_pk, qty):
    qty = int(qty)
    product = get_object_or_404(Product, pk=product_pk)
    if product.quantity >= qty:
        cart = Cart.objects.get(user=request.user, ordered=False)
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
        if created:
            cart_item.quantity = qty
            cart_item.save()
        else:
            cart_item.quantity += qty
            cart_item.save()
        cart_item.product.quantity -= qty
        cart_item.product.save()

        cart.clean()
        messages.add_message(request, messages.SUCCESS, "Product has been added to cart!", fail_silently=True)
    else:
        messages.add_message(request, messages.WARNING, "Shortage of products in stock", fail_silently=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, item_pk, qty):
    qty = int(qty)
    cart = Cart.objects.get(user=request.user, ordered=False)
    cart_item = CartItem.objects.get(pk=item_pk)
    cart_item.product.quantity += qty
    cart_item.product.save()

    if cart_item.quantity == qty:
        cart_item.delete()
    else:
        cart_item.quantity -= qty
        cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_cart(request, pk):
    cart = Cart.objects.get(pk=pk)
    for item in cart.items.all():
        item.product.quantity += item.quantity
        item.product.save()
        item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
