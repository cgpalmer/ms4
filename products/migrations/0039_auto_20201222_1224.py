# Generated by Django 3.1.1 on 2020-12-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20201215_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='cd4b03d1-f988-479a-b6ac-37621977450f', max_length=254),
        ),
    ]
