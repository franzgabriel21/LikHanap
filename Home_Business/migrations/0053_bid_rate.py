# Generated by Django 2.2.7 on 2020-08-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0052_portfolio_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='rate',
            field=models.CharField(default='', max_length=100, verbose_name='Settled Rate (How much are you willing to pay for this project?)'),
        ),
    ]
