# Generated by Django 2.2.7 on 2020-08-21 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home_Business', '0111_auto_20200821_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.CharField(choices=[('☆☆☆☆☆', '☆☆☆☆☆'), ('★☆☆☆☆', '★☆☆☆☆'), ('★★☆☆☆', '★★☆☆☆'), ('★★★☆☆', '★★★☆☆'), ('★★★★☆', '★★★★☆')], default='☆☆☆☆☆', max_length=30, verbose_name='Choose a Rating:'),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Report', models.TextField(verbose_name='Report your complain about this artist:')),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
