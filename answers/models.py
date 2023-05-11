from django.db import models


# Create your models here.
class Answer(models.Model):
    user_id = models.IntegerField(default=1001)
    question = models.OneToOneField("questions.Question", on_delete=models.CASCADE)
    # score = models.ForeignKey("scores.Score", on_delete=models.CASCADE)
    question_option = models.OneToOneField(
        "questions_options.QuestionOption", on_delete=models.CASCADE
    )
