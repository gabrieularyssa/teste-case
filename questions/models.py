from django.db import models


# Create your models here.
class Question(models.Model):
    content = models.CharField(max_length=300)