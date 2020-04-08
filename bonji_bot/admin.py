from django.contrib import admin
from bonji_bot.models import TelegramCartItem, TelegramCustomer, TelegramCart

@admin.register(TelegramCustomer)
class TelegramCustomerAdmin(admin.ModelAdmin):

    list_display = ["__str__", "first_name", "last_name", "phone_number", "email"]

admin.site.register(TelegramCart)
admin.site.register(TelegramCartItem)
