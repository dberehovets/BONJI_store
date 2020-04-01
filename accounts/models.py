from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class MyUser(User, PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"

    class Meta:
        verbose_name = 'Customer'



# SUBSCRIBERS
class Subscriber(models.Model):
    email = models.EmailField(max_length=100, verbose_name='', unique=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email
