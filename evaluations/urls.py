from django.urls import path
from . import views

urlpatterns = [
    path("evaluations/", views.EvaluationView.as_view()),
]
