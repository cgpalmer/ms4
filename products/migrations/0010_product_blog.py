# Generated by Django 3.1.1 on 2020-10-23 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201022_2231'),
        ('products', '0009_remove_product_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog'),
        ),
    ]
