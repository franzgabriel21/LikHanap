# Generated by Django 2.2.7 on 2020-08-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0054_bid_business_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Ongoing', max_length=30, verbose_name='Your Project Status'),
        ),
    ]