# Generated by Django 2.2.7 on 2020-04-14 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0042_auto_20200414_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
