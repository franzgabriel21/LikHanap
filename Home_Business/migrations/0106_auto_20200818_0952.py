# Generated by Django 2.2.7 on 2020-08-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0105_auto_20200818_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='b1image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 1 image'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='b2image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 2 image'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='b3image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 3 image'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='overallrating',
            field=models.ImageField(default='R-0.png', upload_to='rating', verbose_name='Overall Rating'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='r1',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 1'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='r2',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 2'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='r3',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 3'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='b1image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 1 image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='b2image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 2 image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='b3image',
            field=models.ImageField(default='blank.png', upload_to='business_image_feedbacks', verbose_name='Business 3 image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='overallrating',
            field=models.ImageField(default='R-0.png', upload_to='rating', verbose_name='Overall Rating'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='r1',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 1'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='r2',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 2'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='r3',
            field=models.ImageField(default='plain.png', upload_to='rating', verbose_name='Rating 3'),
        ),
    ]
