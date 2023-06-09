from django.db import models


# Create your models here.
class Answer(models.Model):
    user_id = models.IntegerField(default=1001)
    evaluation = models.ForeignKey("evaluations.Evaluation", on_delete=models.CASCADE)
    question = models.ForeignKey("questions.Question", on_delete=models.CASCADE)
    # score = models.ForeignKey("scores.Score", on_delete=models.CASCADE)
    question_option = models.ForeignKey(
        "questions_options.QuestionOption", on_delete=models.CASCADE
    )
