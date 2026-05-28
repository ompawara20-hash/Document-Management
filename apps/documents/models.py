from django.db import models
from .validators import (
    validate_file_type,
    validate_file_size
)

class Document(models.Model):

    title = models.CharField(
        max_length=255
    )

    file = models.FileField(

    upload_to='documents/',

    validators=[
        validate_file_type,
        validate_file_size
    ]
    )

    file_type = models.CharField(
        max_length=50
    )

    related_module = models.CharField(
        max_length=100
    )

    related_id = models.IntegerField()

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title