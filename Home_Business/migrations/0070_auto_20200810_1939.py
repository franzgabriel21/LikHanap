# Generated by Django 2.2.7 on 2020-08-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0069_auto_20200810_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcontract',
            name='category',
            field=models.CharField(choices=[('WEB DESIGNS', 'WEB DESIGNS')], default='WEB DESIGNS', max_length=30, verbose_name='Project Category'),
        ),
    ]
