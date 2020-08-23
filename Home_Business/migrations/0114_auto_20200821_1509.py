# Generated by Django 2.2.7 on 2020-08-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0113_report_artist_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.CharField(choices=[('☆☆☆☆☆', '☆☆☆☆☆'), ('★☆☆☆☆', '★☆☆☆☆'), ('★★☆☆☆', '★★☆☆☆'), ('★★★☆☆', '★★★☆☆'), ('★★★★☆', '★★★★☆'), ('★★★★★', '★★★★★')], default='☆☆☆☆☆', max_length=30, verbose_name='Choose a Rating:'),
        ),
    ]
