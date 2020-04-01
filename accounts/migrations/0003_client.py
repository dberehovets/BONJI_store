# Generated by Django 3.0.4 on 2020-03-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200328_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=30)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics/')),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
    ]
