# Generated by Django 5.1.3 on 2024-11-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]