# Generated by Django 3.0.6 on 2020-07-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pariwisataapi', '0002_auto_20200717_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='pariwisata',
            name='images',
            field=models.ImageField(default='', upload_to='', verbose_name='images/'),
        ),
    ]
