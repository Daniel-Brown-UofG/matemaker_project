# Generated by Django 2.2.17 on 2021-04-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matemaker', '0008_remove_interest_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='slug',
            field=models.SlugField(default='temp', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
