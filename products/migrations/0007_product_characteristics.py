# Generated by Django 3.0.4 on 2020-03-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200326_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.TextField(blank=True),
        ),
    ]
