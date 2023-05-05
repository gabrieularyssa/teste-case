from django.urls import path
from . import views

urlpatterns = [
    path(
        "submeter/",
        views.AnswerView.as_view(),
    )
]
