# Generated by Django 2.2.7 on 2020-08-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0098_auto_20200817_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='overallrating',
            field=models.ImageField(default='plain.png', upload_to='artist_overall_rating', verbose_name='Overall Rating'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='overallrating',
            field=models.ImageField(default='plain.png', upload_to='artist_overall_rating', verbose_name='Overall Rating'),
        ),
    ]
