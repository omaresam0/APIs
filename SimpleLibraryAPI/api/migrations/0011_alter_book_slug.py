# Generated by Django 5.1.3 on 2024-11-23 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0010_remove_book_id_alter_book_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="slug",
            field=models.SlugField(
                editable=False, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
