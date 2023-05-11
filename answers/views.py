from rest_framework.views import APIView, Request, Response, status
from answers.serializers import AnswerSerializer


# Create your views here.
class AnswerView(APIView):
    def get(self, request: Request) -> Response:
        return Response({"message": "Ola GET!"})

    def post(self, request: Request) -> Response:

        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
