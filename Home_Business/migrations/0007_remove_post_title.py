# Generated by Django 2.2.7 on 2020-02-09 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0006_auto_20200208_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]