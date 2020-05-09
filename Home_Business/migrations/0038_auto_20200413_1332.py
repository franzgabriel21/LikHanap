# Generated by Django 2.2.7 on 2020-04-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0037_auto_20200413_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santor', 'Santor')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santor', 'Santor')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santor', 'Santor')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AlterField(
            model_name='post',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santor', 'Santor')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
    ]
