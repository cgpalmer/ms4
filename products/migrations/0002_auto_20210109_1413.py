# Generated by Django 3.1.1 on 2021-01-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upload',
            name='sku',
            field=models.CharField(default='7684240e-b791-470e-ae68-58f4b7163b20', max_length=254),
        ),
    ]