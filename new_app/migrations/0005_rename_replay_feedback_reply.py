# Generated by Django 4.2.13 on 2024-06-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0004_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='replay',
            new_name='reply',
        ),
    ]
