# Generated by Django 3.0.4 on 2020-03-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='No Image', upload_to='products/images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_extra',
            field=models.CharField(blank=True, choices=[('sale', 'Sale'), ('new', 'New'), ('hot', 'Hot')], max_length=5),
        ),
    ]
