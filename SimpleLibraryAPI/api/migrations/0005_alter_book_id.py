# Generated by Django 5.1.3 on 2024-11-22 23:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
