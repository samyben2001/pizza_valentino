# Generated by Django 3.2.12 on 2022-02-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='ingredient',
            field=models.ManyToManyField(to='menu.Ingredient'),
        ),
        migrations.AlterField(
            model_name='pates',
            name='ingredient',
            field=models.ManyToManyField(to='menu.Ingredient'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='ingredient',
            field=models.ManyToManyField(to='menu.Ingredient'),
        ),
    ]
