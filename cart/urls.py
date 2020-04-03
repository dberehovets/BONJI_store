from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('product/<product_pk>/<qty>', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_pk>/<qty>', views.remove_from_cart, name='remove_from_cart'),
    path('clear/<pk>', views.clear_cart, name='clear_cart'),
    path('<pk>/', views.CartDetail.as_view(), name='cart_detail'),
    path('checkout/<pk>', views.CheckOut.as_view(), name='checkout')
]
