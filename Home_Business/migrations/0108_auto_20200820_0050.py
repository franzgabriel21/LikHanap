# Generated by Django 2.2.7 on 2020-08-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0107_auto_20200818_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='artist_username',
            field=models.CharField(default='sharlot', max_length=100, verbose_name='Send this feedback to:'),
        ),
    ]
