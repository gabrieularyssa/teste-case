from rest_framework.views import APIView, Request, Response, status
from answers.serializers import AnswerSerializer
from answers.models import Answer

import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from evaluations.models import Evaluation, EvaluationQuestions
from questions_options.models import QuestionOption
from scores.models import Score


# Create your views here.
class AnswerView(APIView):
    def get(self, request: Request) -> Response:
        return Response({"message": "Ola GET!"})

    def post(self, request: Request) -> Response:
        body = json.loads(request.body)
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_id = 1001
        evaluation_id = body.get("evaluation_id")
        evaluation = get_object_or_404(
            Evaluation,
            id=evaluation_id,
        )
        questions = body.get("questions")
        question_id = [item["id"] for item in questions]

        answers = Answer.objects.filter(user_id=user_id, question_id__in=question_id)
        total_score = 0
        for answer in answers:
            question_option = get_object_or_404(
                QuestionOption,
                id=answer.question_option_id,
            )
            if question_option.correct:
                question_score = EvaluationQuestions.objects.get(
                    evaluations_id=evaluation_id, questions_id=answer.question_id
                ).score
                total_score += question_score

        # print(total_score)
        score, created = Score.objects.get_or_create(
            user_id=user_id,
            evaluation_id=evaluation_id,
        )
        if not created:
            score.total_score = total_score
            score.save()
        data = {
            "score_id": score.id,
            "total_score": total_score,
        }

        # Calculo do score total

        # return Response(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(data)
