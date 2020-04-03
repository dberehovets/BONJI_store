from django import forms

class CheckOutForm(forms.Form):
    PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('ccard', 'Credit Cart')
    )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=100)
    shipping_address = forms.CharField(max_length=200)
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)
