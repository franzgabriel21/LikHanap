# Generated by Django 2.2.7 on 2020-02-20 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home_Business', '0014_auto_20200218_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30)),
                ('location', models.CharField(choices=[('Malolos, Bungahan', 'Malolos, Bungahan'), ('Malolos, Longos', 'Malolos, Longos'), ('Malolos, Caliligawan', 'Malolos, Caliligawan'), ('Malolos, Tikay', 'Malolos, Tikay'), ('Malolos, Santol', 'Malolos, Santol')], default='Malolos, Bungahan', max_length=30)),
                ('artist', models.CharField(max_length=100)),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]