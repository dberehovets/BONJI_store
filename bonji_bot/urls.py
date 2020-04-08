from django.urls import path
from bonji_bot.views import UpdateBot, Check
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

app_name = "bonji_bot"

urlpatterns = [
    path("c04a4995-a7e2-4bf5-b8ab-d7599105d1d1/", csrf_exempt(UpdateBot.as_view()), name='update'),
    path("", csrf_exempt(Check.as_view()), name='check'),
]
