# Generated by Django 2.2.7 on 2020-04-13 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0034_auto_20200410_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='location',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='location',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.AddField(
            model_name='apply',
            name='city',
            field=models.CharField(choices=[('malolos', 'Malolos')], default='Malolos', max_length=30, verbose_name='Enter your city residence'),
        ),
        migrations.AddField(
            model_name='apply',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santol', 'Santol')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AddField(
            model_name='bid',
            name='city',
            field=models.CharField(choices=[('malolos', 'Malolos')], default='Malolos', max_length=30, verbose_name='Enter your city residence'),
        ),
        migrations.AddField(
            model_name='bid',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santol', 'Santol')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='city',
            field=models.CharField(choices=[('malolos', 'Malolos')], default='Malolos', max_length=30, verbose_name='Enter your city residence'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santol', 'Santol')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(choices=[('malolos', 'Malolos')], default='Malolos', max_length=30, verbose_name='Enter your city residence'),
        ),
        migrations.AddField(
            model_name='post',
            name='street',
            field=models.CharField(choices=[('bungahan', 'Bungahan'), ('longos', 'Longos'), ('caliligawan', 'Caliligawan'), ('tikay', 'Tikay'), ('santol', 'Santol')], default='Tikay', max_length=30, verbose_name='Enter your barangay'),
        ),
    ]
