# Generated by Django 5.1.3 on 2024-11-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_alter_book_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]