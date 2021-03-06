# Generated by Django 2.2.7 on 2020-08-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0089_auto_20200812_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='certificate',
            field=models.ImageField(default='unlock.png', upload_to='certificates', verbose_name='Ownership Certificate'),
        ),
        migrations.AddField(
            model_name='post',
            name='contract',
            field=models.ImageField(default='contract.png', upload_to='contract', verbose_name='Contract Agreement'),
        ),
    ]
