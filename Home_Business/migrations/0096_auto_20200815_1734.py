# Generated by Django 2.2.7 on 2020-08-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0095_likhanapfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='theme',
            field=models.CharField(choices=[('MINIMALIST', 'MINIMALIST'), ('MODERN', 'MODERN'), ('INNOVATIVE', 'INNOVATIVE')], default='MINIMALIST', max_length=30, verbose_name='What theme best suits your style?'),
        ),
        migrations.AddField(
            model_name='bid',
            name='theme',
            field=models.CharField(choices=[('MINIMALIST', 'MINIMALIST'), ('MODERN', 'MODERN'), ('INNOVATIVE', 'INNOVATIVE')], default='MINIMALIST', max_length=30, verbose_name='What theme best suits your style?'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='theme',
            field=models.CharField(choices=[('MINIMALIST', 'MINIMALIST'), ('MODERN', 'MODERN'), ('INNOVATIVE', 'INNOVATIVE')], default='MINIMALIST', max_length=30, verbose_name='What theme best suits your style?'),
        ),
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.CharField(choices=[('MINIMALIST', 'MINIMALIST'), ('MODERN', 'MODERN'), ('INNOVATIVE', 'INNOVATIVE')], default='MINIMALIST', max_length=30, verbose_name='What theme best suits your style?'),
        ),
    ]
