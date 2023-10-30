import os

from django.conf import settings
from django.views.generic.edit import FormView

from ..forms import QuestionGalleryForm


class QuestionGalleryCreateView(FormView):
    template_name = "pages/index.html"
    form_class = QuestionGalleryForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        # Get the instance without saving to the database yet
        gallery_instance = form.save(commit=False)

        # Rename the question_file and answer_file fields
        for field_name in ["question_file", "answer_file"]:
            file_field = getattr(gallery_instance, field_name)
            if file_field:
                # Get the extension of the file
                extension = os.path.splitext(file_field.name)[1]
                # Rename the file based on the question_text value
                new_file_name = "{}{}".format(
                    gallery_instance.question_text, extension
                )
                file_field.name = new_file_name

        # Now save the instance to the database
        gallery_instance.save()

        text_file_name = os.path.join(
            settings.BASE_DIR,
            "media/answers",
            "{}.txt".format(gallery_instance.question_text),
        )

        with open(text_file_name, "w") as file:
            file.write(str(gallery_instance.answer_integer))

        return super().form_valid(form)
