# Generated by Django 2.2.7 on 2020-08-18 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0103_auto_20200818_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description1',
            field=models.TextField(blank=True, verbose_name='Project Description (What can you say about this project?)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description2',
            field=models.TextField(blank=True, verbose_name='Project Description (What can you say about this project?)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description3',
            field=models.TextField(blank=True, verbose_name='Project Description (What can you say about this project?)'),
        ),
    ]