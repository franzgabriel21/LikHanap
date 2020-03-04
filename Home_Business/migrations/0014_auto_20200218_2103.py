# Generated by Django 2.2.7 on 2020-02-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0013_auto_20200217_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30),
        ),
    ]