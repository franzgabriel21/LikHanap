# Generated by Django 2.2.7 on 2020-08-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0053_bid_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='business_username',
            field=models.CharField(default='', max_length=100, verbose_name='Please type your username'),
        ),
    ]
