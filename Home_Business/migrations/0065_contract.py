# Generated by Django 2.2.7 on 2020-08-10 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home_Business', '0064_remove_bid_business_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('LOGO', 'LOGO'), ('BANNER ADS', 'BANNER ADS'), ('SIGNAGE', 'SIGNAGE'), ('WEB DESIGNS', 'WEB DESIGNS')], default='LOGO', max_length=30, verbose_name='Choose your project category')),
                ('businessname', models.CharField(max_length=100, verbose_name='Business Name')),
                ('ownername', models.CharField(max_length=100, verbose_name='Business Owner Name')),
                ('address', models.CharField(max_length=100, verbose_name='Business Owner Address')),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
