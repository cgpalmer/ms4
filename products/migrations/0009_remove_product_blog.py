# Generated by Django 3.1.1 on 2020-10-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201007_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='blog',
        ),
    ]