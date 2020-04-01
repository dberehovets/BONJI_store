from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from categories.models import Category

from accounts.forms import SubscriberForm
from accounts.models import Subscriber

from django.contrib import messages

# Create your views here.
class ListCategories(ListView):
    model = Category

class DetailCategory(DetailView):
    model = Category
