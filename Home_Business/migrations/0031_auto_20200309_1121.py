# Generated by Django 2.2.7 on 2020-03-09 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0030_employ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accept',
            name='Business_username',
            field=models.CharField(default='', max_length=100, verbose_name='Please type your commission partner'),
        ),
        migrations.AlterField(
            model_name='accept',
            name='Message',
            field=models.TextField(verbose_name='Message (Enter your message here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Background',
            field=models.TextField(verbose_name='Background (Tell us about your previous works and experiences)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Business_username',
            field=models.CharField(max_length=100, verbose_name='Please type your commission partner'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Expertise',
            field=models.CharField(max_length=100, verbose_name='Expertise (Name your best skill)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image1',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image2',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image3',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='location',
            field=models.CharField(choices=[('Malolos, Bungahan', 'Malolos, Bungahan'), ('Malolos, Longos', 'Malolos, Longos'), ('Malolos, Caliligawan', 'Malolos, Caliligawan'), ('Malolos, Tikay', 'Malolos, Tikay'), ('Malolos, Santol', 'Malolos, Santol')], default='Malolos, Bungahan', max_length=30, verbose_name='Enter your current location'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='artist_username',
            field=models.CharField(max_length=100, verbose_name='Please type your commission partner'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='content',
            field=models.TextField(verbose_name='Content (Give a thorough project description)'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='post_pics', verbose_name='Attach your image here'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='location',
            field=models.CharField(choices=[('Malolos, Bungahan', 'Malolos, Bungahan'), ('Malolos, Longos', 'Malolos, Longos'), ('Malolos, Caliligawan', 'Malolos, Caliligawan'), ('Malolos, Tikay', 'Malolos, Tikay'), ('Malolos, Santol', 'Malolos, Santol')], default='Malolos, Bungahan', max_length=30, verbose_name='Enter your current location'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title (Name your project commission)'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='Message',
            field=models.TextField(verbose_name='Message (Enter your message here)'),
        ),
        migrations.AlterField(
            model_name='employ',
            name='artist_username',
            field=models.CharField(default='', max_length=100, verbose_name='Please type your commission partner'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Background',
            field=models.TextField(verbose_name='Background (Tell us about your previous works and experiences)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Expertise',
            field=models.CharField(max_length=100, verbose_name='Expertise (Name your best skill)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image1',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(default='plain.jpg', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='location',
            field=models.CharField(choices=[('Malolos, Bungahan', 'Malolos, Bungahan'), ('Malolos, Longos', 'Malolos, Longos'), ('Malolos, Caliligawan', 'Malolos, Caliligawan'), ('Malolos, Tikay', 'Malolos, Tikay'), ('Malolos, Santol', 'Malolos, Santol')], default='Malolos, Bungahan', max_length=30, verbose_name='Enter your current location'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('LOGO', 'LOGO'), ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'), ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'), ('INVITATION LAYOUT', 'INVITATION LAYOUT'), ('INTERIOR DESIGN', 'INTERIOR DESIGN')], default='LOGO', max_length=30, verbose_name='Choose your project category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content (Give a thorough project description)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='plain.jpg', upload_to='post_pics', verbose_name='Attach your image here'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('Malolos, Bungahan', 'Malolos, Bungahan'), ('Malolos, Longos', 'Malolos, Longos'), ('Malolos, Caliligawan', 'Malolos, Caliligawan'), ('Malolos, Tikay', 'Malolos, Tikay'), ('Malolos, Santol', 'Malolos, Santol')], default='Malolos, Bungahan', max_length=30, verbose_name='Enter your current location'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title (Name your project commission)'),
        ),
    ]
