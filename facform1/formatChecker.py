from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize=value.size

    if filesize > 20971520:
        raise forms.ValidationError("The maximum file size that can be uploaded is 20MB")
    else:
        return value
