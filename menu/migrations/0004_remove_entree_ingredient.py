# Generated by Django 3.2.12 on 2022-02-21 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_ingredient_prix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entree',
            name='ingredient',
        ),
    ]
