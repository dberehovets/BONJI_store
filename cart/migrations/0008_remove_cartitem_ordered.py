# Generated by Django 3.0.4 on 2020-04-02 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20200402_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='ordered',
        ),
    ]
