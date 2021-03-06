# Generated by Django 3.0.4 on 2020-03-26 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20200326_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('old_price', models.FloatField(blank=True)),
                ('new_price', models.FloatField()),
                ('availability', models.CharField(choices=[('in', 'In Stock'), ('no', 'Non-Available')], default='in', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.Category')),
            ],
        ),
    ]
