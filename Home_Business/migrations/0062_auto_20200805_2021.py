# Generated by Django 2.2.7 on 2020-08-05 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0061_auto_20200805_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='verified',
            field=models.CharField(choices=[('---', '---')], default='---', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='verified',
            field=models.CharField(choices=[('---', '---')], default='---', max_length=100),
        ),
    ]
