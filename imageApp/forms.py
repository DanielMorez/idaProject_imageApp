from django import forms
from django.core.exceptions import ValidationError

from .models import Image


class ImageForm(forms.Form):

    image_url = forms.URLField(label=("Ссылка"), required=False)
    image_file = forms.FileField(label=("Файл"), required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def clean(self):
        cleaned_data = super(ImageForm, self).clean()
        image_url = cleaned_data.get('image_url')
        image_file = cleaned_data.get('image_file')

        if (not image_url and not image_file) or (image_file and image_url):
            raise ValidationError(
                    "Incorrect send image. "
                    "You can send only image file or image url."
                )


class ChangeImageSizeForm(forms.Form):

    width = forms.IntegerField(label='Ширина', required=False)
    height = forms.IntegerField(label='Высота', required=False)

    def clean(self):
        cleaned_data = super(ChangeImageSizeForm, self).clean()
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')

        if not width and not height:
            raise ValidationError(
                    "Incorrect send image size. "
                    "You can change width or height or width and height. "
                )