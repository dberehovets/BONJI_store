from django.views.generic import TemplateView
from django.shortcuts import redirect

from accounts.forms import SubscriberForm
from accounts.models import Subscriber

from products.models import Product

from django.contrib import messages

from random import shuffle
from django.core.mail import send_mail

class HomePage(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        form = SubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.get_or_create(**form.cleaned_data)
        messages.add_message(request, messages.SUCCESS, "You are subscribed!")
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list(Product.objects.all())

        shuffle(products)

        if len(products) >= 8:
            products = products[:8]

        context['products'] = products
        return context


class ContactPage(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        # name = request.POST.get('name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject') or "New message"
        # message = name + " " + last_name + " wrote \n" + request.POST.get('message')

        # send_mail(subject, message, email, ['dberehovets@gmail.com'])
        messages.add_message(request, messages.SUCCESS, "Your email has been sent. Thank you!")
        return redirect('contact')
