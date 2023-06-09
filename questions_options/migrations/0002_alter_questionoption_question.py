# Generated by Django 4.2 on 2023-05-05 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0001_initial"),
        ("questions_options", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionoption",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question",
                to="questions.question",
            ),
        ),
    ]
