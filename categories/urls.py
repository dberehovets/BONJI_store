from django.urls import path, include

from categories import views

app_name = 'categories'


urlpatterns = [
    path('api/', views.CategoryApiList.as_view()),
]