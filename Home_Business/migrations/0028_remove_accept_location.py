# Generated by Django 2.2.7 on 2020-02-29 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0027_remove_accept_emailaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept',
            name='location',
        ),
    ]
