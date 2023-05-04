from rest_framework import serializers
from questions_options.models import QuestionOption
from questions.serializers import QuestionSerializer


class QuestionOptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(max_length=300)
    sequence = serializers.CharField(max_length=5)
    correct = serializers.BooleanField(default=False)
    question = serializers.QuestionSerializer()
