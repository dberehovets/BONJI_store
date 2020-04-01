from django import forms
from accounts.models import Subscriber, MyUser

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'newsletter_input'})
        }


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        model = MyUser
