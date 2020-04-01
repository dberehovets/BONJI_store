# Generated by Django 3.0.4 on 2020-03-31 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200328_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=10, null=True),
        ),
    ]
