# Generated by Django 2.2.7 on 2020-08-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0087_auto_20200812_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='prescreen',
            field=models.ImageField(default='prescreen.png', upload_to='portfolio_pics', verbose_name='Likhanap Pre-screening Results'),
        ),
    ]
