# Generated by Django 3.2.12 on 2022-02-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_entree_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pates',
            name='ingredient',
        ),
    ]
