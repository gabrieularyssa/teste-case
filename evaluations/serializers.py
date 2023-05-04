from rest_framework import serializers
from evaluations.models import Evaluation


class EvaluationQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    evaluations = serializers.IntegerField(read_only=True)
    questions = serializers.IntegerField(read_only=True)
    score = serializers.IntegerField()


class EvaluationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)

    # evaluations_questions = serializers.EvaluationQuestionSerializer()
