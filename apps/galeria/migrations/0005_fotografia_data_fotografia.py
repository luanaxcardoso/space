# Generated by Django 5.0.3 on 2024-03-09 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0004_fotografia_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotografia",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
