from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
import random

from products.models import Product
from categories.models import Category

from accounts.forms import SubscriberForm
from accounts.models import Subscriber

from django.contrib import messages

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from products import serializers


class ProductDetail(DetailView):
    model = Product

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        qty = request.POST.get('qty')

        if email:
            form = SubscriberForm(request.POST)
            if form.is_valid():
                Subscriber.objects.get_or_create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, "You are subscribed!", fail_silently=True)
        elif int(qty) > 0:
            return redirect('cart:add_to_cart', product_pk=self.get_object().pk, qty=qty)
        elif qty == "0":
            messages.add_message(request, messages.WARNING, "Change product quantity!", fail_silently=True)
        return redirect('products:product_detail', pk=self.get_object().pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_products = list(Product.objects.filter(category=self.get_object().category))
        random.shuffle(related_products)
        context['related_products'] = related_products[:4]
        return context


class ProductList(ListView):
    model = Product
    paginate_by = 12

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs['category_pk'])
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_pk'])
        return context

    def post(self, request, *args, **kwargs):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.get_or_create(**form.cleaned_data)
        messages.add_message(request, messages.SUCCESS, "You are subscribed!", fail_silently=True)
        return redirect('products:product_list', category_pk=self.kwargs['category_pk'])


class ProductApiList(APIView):

    def get(self, request, category_pk, format=None):
        category = generics.get_object_or_404(Category, pk=category_pk)
        products = Product.objects.filter(category=category)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductApiDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
