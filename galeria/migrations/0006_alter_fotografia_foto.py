# Generated by Django 5.0.3 on 2024-03-10 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0005_fotografia_data_fotografia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]
