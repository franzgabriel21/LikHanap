# Generated by Django 2.2.7 on 2020-08-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0079_feedback_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='certificate',
        ),
        migrations.AddField(
            model_name='bid',
            name='certificate',
            field=models.ImageField(default='plain.jpg', upload_to='certificates', verbose_name='Ownership Certificate'),
        ),
    ]
