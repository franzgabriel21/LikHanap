# Generated by Django 2.2.7 on 2020-08-10 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home_Business', '0070_auto_20200810_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('GRAPHIC DESIGNS', 'GRAPHIC DESIGNS')], default='GRAPHIC DESIGNS', max_length=30, verbose_name='Project Category')),
                ('businessname', models.CharField(default='', max_length=100, verbose_name='Business Name')),
                ('ownername', models.CharField(default='', max_length=100, verbose_name='Business Owner Name')),
                ('address', models.CharField(default='', max_length=100, verbose_name='Business Owner Address')),
                ('image', models.ImageField(default='plain.jpg', upload_to='post_pics', verbose_name='Please attach your valid signature')),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
