from categories.models import Category
from products.models import Product
from accounts.forms import SubscriberForm
from cart.models import Cart
from django.db import models

from random import shuffle

def category_menu(request):

    link_menu = Category.objects.all()
    subscribe_form = SubscriberForm()

    offers_pk = Category.objects.get(title="Offers").pk
    accessories_pk = Category.objects.get(title="Accessories").pk

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, ordered=False)
        cart_qty = cart.items.count()
        cart_pk = cart.pk
    else:
        cart_qty = 0
        cart_pk = None

    return {
        'link_menu': link_menu,
        'subscribe_form': subscribe_form,
        'offers_pk': offers_pk,
        'accessories_pk': accessories_pk,
        'cart_qty': cart_qty,
        'cart_pk': cart_pk,
    }


from django.conf import settings

def ssl_media(request):

  if request.is_secure():
    ssl_media_url = settings.MEDIA_URL.replace('http://','https://')
  else:
    ssl_media_url = settings.MEDIA_URL

  return {'MEDIA_URL': ssl_media_url}
