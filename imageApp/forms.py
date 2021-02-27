from django import forms
from django.core.exceptions import ValidationError

from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        image_url = cleaned_data.get('image-url')
        image_file = cleaned_data.get('image-file')

        if (not image_url and not image_file) or (image_file and image_url):
            raise ValidationError(
                    "Incorrect send image. "
                    "You can send only image file or image url."
                )
