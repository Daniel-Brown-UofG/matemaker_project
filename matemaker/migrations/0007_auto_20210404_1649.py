# Generated by Django 2.2.17 on 2021-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matemaker', '0006_auto_20210404_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='interest',
            name='slug',
            field=models.SlugField(),
        ),
    ]
