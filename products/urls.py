from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<category_pk>/', views.ProductList.as_view(), name='product_list'),
    path('api/<int:pk>/', views.ProductApiDetail.as_view()),
    path('api/category/<int:category_pk>/', views.ProductApiList.as_view()),
]
