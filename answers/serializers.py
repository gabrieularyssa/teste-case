from rest_framework import serializers
from answers.models import Answer
from questions.serializers import QuestionSerializer
from questions_options.serializers import QuestionOptionSerializer


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=1001)
    question = serializers.QuestionSerializer()
    question_option = serializers.QuestionOptionSerializer()
