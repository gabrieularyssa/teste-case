from django.db import models


# Create your models here.
class Evaluation(models.Model):
    title = models.CharField(max_length=50)

    questions = models.ManyToManyField(
        "questions.Question",
        related_name="evaluations",
    )

    def __repr__(self) -> str:
        return f"<Evaluation {self.id} - {self.title}>"
