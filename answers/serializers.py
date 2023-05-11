from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.exceptions import NotFound

from answers.models import Answer
from evaluations.models import Evaluation
from questions.models import Question

from questions.serializers import QuestionSerializer
from questions_options.serializers import QuestionOptionSerializer
from scores.serializers import ScoreSerializer
from evaluations.serializers import EvaluationSerializer


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(required=False, default=1001)
    question = QuestionSerializer(required=False)
    question_option = QuestionOptionSerializer(required=False)
    # score = ScoreSerializer(required=False, default=0)
    evaluation = EvaluationSerializer(required=False)

    question_id = serializers.IntegerField()
    question_option_id = serializers.IntegerField()
    evaluation_id = serializers.IntegerField()
    # score_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Answer
        fields = [
            "id",
            "question_id",
            "question_option_id",
            "evaluation_id",
            # "score_id",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        body = {**validated_data}
        evaluation = body.get("evaluation_id")
        question = body.get("question_id")
        question_option = body.get("question_option_id")

        # score_id = body.get("score_id")

        try:
            evaluation = get_object_or_404(Evaluation, pk=evaluation)
        except Http404:
            raise NotFound("Evaluation not found")

        try:
            question = get_object_or_404(Question, pk=question)
        except Http404:
            raise NotFound("Question not found")

        answer = Answer.objects.create(**body)

        return answer
