# Generated by Django 3.1.1 on 2020-10-06 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='story',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='friendly_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
    ]