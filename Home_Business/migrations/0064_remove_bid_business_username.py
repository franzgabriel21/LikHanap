# Generated by Django 2.2.7 on 2020-08-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0063_auto_20200808_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='business_username',
        ),
    ]
