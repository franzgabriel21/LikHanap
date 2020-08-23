# Generated by Django 2.2.7 on 2020-08-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0047_auto_20200803_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('VISUAL ARTS', 'VISUAL ARTS'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('VISUAL ARTS', 'VISUAL ARTS'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('VISUAL ARTS', 'VISUAL ARTS'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('VISUAL ARTS', 'VISUAL ARTS'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='verifiedpost',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('VISUAL ARTS', 'VISUAL ARTS'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
    ]
