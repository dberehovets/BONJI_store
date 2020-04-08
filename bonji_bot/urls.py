from django.urls import path
from bonji_bot.views import UpdateBot, Check
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

app_name = "bonji_bot"

urlpatterns = [
    path(f"/{settings.TOKEN}", csrf_exempt(UpdateBot.as_view()), name='update'),
    path("", csrf_exempt(Check.as_view()), name='check'),
]
