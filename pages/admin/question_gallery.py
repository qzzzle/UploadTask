from django.contrib import admin

from ..models import QuestionGallery


@admin.register(QuestionGallery)
class QuestionGalleryAdmin(admin.ModelAdmin):
    list_display = ["question_text", "answer_integer"]
    list_filter = ["answer_integer"]
    search_fields = ["question_text"]
    fieldsets = [
        ("Question Information", {"fields": ["question_text", "question_file"]}),
        ("Answer Information", {"fields": ["answer_file", "answer_integer"]}),
    ]
