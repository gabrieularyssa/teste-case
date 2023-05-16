from django.db import models

# Create your models here.


class EvaluationQuestions(models.Model):
    evaluations = models.ForeignKey(
        "Evaluation",
        on_delete=models.CASCADE,
    )
    questions = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
    )
    score = models.IntegerField()

    def __repr__(self) -> str:
        return f"<Evaluation_Question {self.id} - {self.score}>"


class Evaluation(models.Model):
    title = models.CharField(max_length=50)

    questions = models.ManyToManyField(
        "questions.Question",
        related_name="evaluations",
        through="EvaluationQuestions",
    )

    def __repr__(self) -> str:
        return f"<Evaluation {self.id} - {self.title}>"
