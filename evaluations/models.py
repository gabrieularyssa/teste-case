from django.db import models


# Create your models here.
class Evaluation(models.Model):
    title = models.CharField(max_length=50)
