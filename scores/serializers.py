from rest_framework import serializers
from scores.models import Score
from evaluations.serializers import EvaluationSerializer


class ScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=1001)
    evaluation = serializers.EvaluationSerializer()
    total_score = serializers.IntegerField()
    finish = serializers.BooleanField()
