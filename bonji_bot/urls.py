from django.urls import path
from bonji_bot.views import BotView
from BONJI_store.settings import TOKEN
from django.views.decorators.csrf import csrf_exempt

app_name = "bonji_bot"

urlpatterns = [
    path(f'/{TOKEN}', csrf_exempt(BotView.as_view()), name='update'),
]
