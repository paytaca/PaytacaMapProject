# Generated by Django 5.0.3 on 2024-04-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaytacaApp', '0005_alter_location_category_alter_location_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
