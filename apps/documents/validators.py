from django.core.exceptions import ValidationError


ALLOWED_FILE_TYPES = [

    'pdf',
    'docx',
    'jpg',
    'jpeg',
    'png'
]


def validate_file_type(file):

    extension = file.name.split('.')[-1].lower()

    if extension not in ALLOWED_FILE_TYPES:

        raise ValidationError(

            f'Unsupported file type: {extension}'
        )

MAX_FILE_SIZE = 10 * 1024 * 1024

def validate_file_size(file):

    if file.size > MAX_FILE_SIZE:

        raise ValidationError(

            'File size exceeds 10 MB'
        )