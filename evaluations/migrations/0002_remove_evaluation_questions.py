# Generated by Django 4.2 on 2023-05-15 19:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("evaluations", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evaluation",
            name="questions",
        ),
    ]