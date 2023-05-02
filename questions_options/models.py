from django.db import models


# Create your models here.
class QuestionOption(models.Model):
    content = models.CharField(max_length=300)
    sequence = models.CharField(max_length=5)
    correct = models.BooleanField(default=False)

    question = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
    )
