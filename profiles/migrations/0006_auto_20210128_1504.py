# Generated by Django 3.1.1 on 2021-01-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210128_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='30de7ef5-55a0-4029-8b1a-0c30fab35975', max_length=254),
        ),
    ]
