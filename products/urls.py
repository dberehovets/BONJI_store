from django.urls import path

from products.views import ProductDetail, ProductList

app_name = 'products'

urlpatterns = [
    path('<pk>/', ProductDetail.as_view(), name='product_detail'),
    path('category/<category_pk>/', ProductList.as_view(), name='product_list'),
]
