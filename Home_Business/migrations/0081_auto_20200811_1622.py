# Generated by Django 2.2.7 on 2020-08-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0080_auto_20200811_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='certificate',
        ),
        migrations.AddField(
            model_name='feedback',
            name='certificate',
            field=models.ImageField(default='plain.jpg', upload_to='certificates', verbose_name='Ownership Certificate'),
        ),
    ]
