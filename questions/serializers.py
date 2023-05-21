from rest_framework import serializers
from questions.models import Question
from .models import Question


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(max_length=300)

    class Meta:
        model = Question
        filds = ["content"]
        read_only_field = ["id"]

    def create(self, validated_data):
        body = {**validated_data}
        content = body.get("content")
        question = Question.objects.create(content=content)

        return question
