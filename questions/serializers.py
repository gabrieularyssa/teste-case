from rest_framework import serializers
from questions.models import Question


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(max_length=300)
