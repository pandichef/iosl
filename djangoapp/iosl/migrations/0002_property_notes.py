# Generated by Django 4.1 on 2024-06-24 06:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("iosl", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="notes",
            field=tinymce.models.HTMLField(default=""),
        ),
    ]
