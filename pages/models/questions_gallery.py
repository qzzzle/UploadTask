from django.db import models


class QuestionGallery(models.Model):
    """
    A model representing a gallery of questions and answers.
    Each gallery has a question text, a question file, an answer file, and an answer integer.
    """

    question_text = models.CharField(
        max_length=255,
        verbose_name="Question Text",
        help_text="Enter the question name here",
    )

    question_file = models.ImageField(
        max_length=200,
        upload_to="pictures/",
        verbose_name="Question File",
        help_text="Upload the question file",
    )

    answer_file = models.ImageField(
        max_length=200,
        upload_to="pictures/",
        verbose_name="Answer File",
        help_text="Upload the answer file",
    )

    answer_integer = models.IntegerField(
        choices=[(i, i) for i in range(1, 5)],
        verbose_name="Answer Integer",
        help_text="Choose an integer as the answer (1 to 4)",
    )

    def __str__(self):
        """
        Returns a string representation of the model instance.
        """
        return self.question_text

    def __repr__(self):
        """
        Returns a formal string representation of the model instance for debugging.
        """
        return f"QuestionGallery(id={self.id}, question_text='{self.question_text}')"

    class Meta:
        verbose_name = "Question Gallery"
        verbose_name_plural = "Question Galleries"
