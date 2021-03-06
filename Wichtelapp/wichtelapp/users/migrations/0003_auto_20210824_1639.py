# Generated by Django 3.2.6 on 2021-08-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210824_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Bild 1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Bild 2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Bild 3'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pinterest',
            field=models.URLField(blank=True, null=True, verbose_name='Link zu deinem Pinterest-Account'),
        ),
    ]
