# Generated by Django 4.2 on 2023-05-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0001_initial"),
        ("evaluations", "0002_remove_evaluation_questions"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="EvaluationQuestion",
            new_name="EvaluationQuestions",
        ),
        migrations.AddField(
            model_name="evaluation",
            name="questions",
            field=models.ManyToManyField(
                related_name="evaluations",
                through="evaluations.EvaluationQuestions",
                to="questions.question",
            ),
        ),
    ]
