from django.urls import path

from .views import QuestionGalleryCreateView

urlpatterns = [
    path("", QuestionGalleryCreateView.as_view(), name="question"),
]
