# Generated by Django 3.2.12 on 2022-02-21 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20220221_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='prix',
        ),
    ]
