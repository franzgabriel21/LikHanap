# Generated by Django 2.2.7 on 2020-08-05 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0057_auto_20200805_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='verifiedpost',
            name='paid',
        ),
    ]
