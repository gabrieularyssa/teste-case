from django.db import models


# Create your models here.
class Score(models.Model):
    user_id = models.IntegerField(default=1001)
    evaluation = models.ForeignKey("evaluations.Evaluation", on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    finish = models.BooleanField(default=False)
