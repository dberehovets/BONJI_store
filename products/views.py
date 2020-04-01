from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
import random

from products.models import Product
from categories.models import Category

from accounts.forms import SubscriberForm
from accounts.models import Subscriber

from django.contrib import messages

# Create your views here.
class ProductDetail(DetailView):
    model = Product

    def post(self, request, *args, **kwargs):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.get_or_create(**form.cleaned_data)
        messages.add_message(request, messages.SUCCESS, "You are subscribed!", fail_silently=True)
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
