# Generated by Django 2.2.7 on 2020-08-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0116_auto_20200823_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='artist_username',
            field=models.CharField(max_length=100, verbose_name='Commission Artist:'),
        ),
        migrations.AlterField(
            model_name='logocertificate',
            name='artistname',
            field=models.CharField(max_length=100, verbose_name='Artist Full Name'),
        ),
        migrations.AlterField(
            model_name='report',
            name='artist_username',
            field=models.CharField(max_length=100, verbose_name='Reported Artist:'),
        ),
        migrations.AlterField(
            model_name='webcertificate',
            name='artistname',
            field=models.CharField(max_length=100, verbose_name='Artist Full Name'),
        ),
    ]
