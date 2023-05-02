from rest_framework.views import APIView, Request, Response, status

# Create your views here.


class EvaluationView(APIView):
    def get(self, request: Request) -> Response:
        return Response({"message": "Ola GET!"})

    def post(self, request: Request) -> Response:
        return Response({"message": "Ola POST!"})
