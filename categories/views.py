from categories.models import Category
from categories.serializers import CategorySerializer

from rest_framework import generics


class CategoryApiList(generics.ListAPIView):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer


