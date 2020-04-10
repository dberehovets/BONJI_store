from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/images")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
