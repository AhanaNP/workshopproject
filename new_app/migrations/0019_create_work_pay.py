# Generated by Django 4.2.13 on 2024-07-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0018_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_work',
            name='pay',
            field=models.IntegerField(default=0),
        ),
    ]
