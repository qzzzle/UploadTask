from django import forms

from ..models import QuestionGallery


class QuestionGalleryForm(forms.ModelForm):
    class Meta:
        model = QuestionGallery
        fields = ["question_text", "question_file", "answer_file", "answer_integer"]
