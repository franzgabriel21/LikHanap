# Generated by Django 2.2.7 on 2020-08-11 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0077_auto_20200811_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agraphiccontract',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='alogocontract',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='awebcontract',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='graphiccontract',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='webcontract',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
    ]