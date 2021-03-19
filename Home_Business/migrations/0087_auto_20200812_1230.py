# Generated by Django 2.2.7 on 2020-08-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_Business', '0086_auto_20200812_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agraphiccontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='alogocontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image1',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image2',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='image3',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='prescreen',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Likhanap Pre-screening Results'),
        ),
        migrations.AlterField(
            model_name='awebcontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='certificate',
            field=models.ImageField(default='unlock.png', upload_to='certificates', verbose_name='Ownership Certificate'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='contract',
            field=models.ImageField(default='plain.png', upload_to='contract', verbose_name='Contract Agreement'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='post_pics', verbose_name='Attach your image here'),
        ),
        migrations.AlterField(
            model_name='graphiccontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='logocertificate',
            name='logo',
            field=models.ImageField(default='plain.png', upload_to='logos', verbose_name='Please your logo image here (Recommended: 800 x 800 px)'),
        ),
        migrations.AlterField(
            model_name='logocontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image1',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image2',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image3',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Image (Attach your previous commissions here)'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='prescreen',
            field=models.ImageField(default='plain.png', upload_to='portfolio_pics', verbose_name='Likhanap Pre-screening Results'),
        ),
        migrations.AlterField(
            model_name='webcontract',
            name='image',
            field=models.ImageField(default='plain.png', upload_to='signatures', verbose_name='Please attach your valid signature (Recommended: .png, 850 x 480 px)'),
        ),
    ]