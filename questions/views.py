from rest_framework.views import APIView, Request, Response, status
from .serializers import QuestionSerializer
from .models import Question

import json


class QuestionView(APIView):
    def get(self, request: Request) -> Response:
        question_obj = Question.objects.all()
        serializer = QuestionSerializer(question_obj, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        body = json.loads(request.body)
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
