# Generated by Django 2.2.7 on 2020-08-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0056_auto_20200804_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='paid',
            field=models.CharField(choices=[('Unpaid', 'Unpaid')], default='Unpaid', max_length=100),
        ),
        migrations.AddField(
            model_name='verifiedpost',
            name='paid',
            field=models.CharField(choices=[('Unpaid', 'Unpaid')], default='Unpaid', max_length=100),
        ),
    ]