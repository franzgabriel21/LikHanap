# Generated by Django 2.2.7 on 2020-04-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verified',
            field=models.CharField(max_length=30),
        ),
    ]
