# Generated by Django 3.1.1 on 2020-10-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201024_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]