import os

from django.shortcuts import render
from django.db import transaction

from .models import Image
from .mixin import DetectedCustomerMixin
from .forms import ImageForm, ChangeImageSizeForm
from .utils import get_remote_image, resize_image

class MainPageView(DetectedCustomerMixin):

    def get(self, request, *args, **kwargs):
        context = {
            'customer': self.owner,
            'images': Image.objects.filter(owner=self.owner)
        }
        return render(request, 'base.html', context)

class UploadImageView(DetectedCustomerMixin):

    form = ImageForm
    success_form = ChangeImageSizeForm

    def get(self, request, *args, **kwargs):
        """ Форма для загрузки изображения """
        return render(request, 'upload.html', {'form': self.form()})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        """ Загрузка изображения """
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            # Если загружен файл
            image_file = form.cleaned_data['image_file']
            if image_file:
                title = form.cleaned_data['image_file'].name
            # Если загружена ссылка на изображение
            else:
                # Если ссылка на изображение валидна
                image_file, title = get_remote_image(form.cleaned_data['image_url'])
            # Если есть, что сохранять, то сохраняем. Иначе возвращаем пустую форму.
            if image_file and title:
                image = Image(
                    title=title,
                    owner=self.owner,
                )
                image.origin.save(title, image_file)   # сохраним оригинал
                image.current.save(title, image.origin)  # редактируемое изображение
                image.save()
                    return render(request, 'changer.html', {'image': image, 'form': self.success_form(), 'access': True})
        return render(request, 'upload.html', {'form': self.form()})


class ChangeImageSizeView(DetectedCustomerMixin):

    form = ChangeImageSizeForm

    def access(self, image):
        return self.owner.id == image.owner.id

    def get(self, request, *args, **kwargs):
        image = Image.objects.filter(id=kwargs['image_id']).first()
        access = self.access(image)  # Проверка на принадлежность пользователю изображения
        return render(request, 'changer.html', {'form': self.form(), 'image': image, 'access': access})

    def post(self, request, *args, **kwargs):
        image = Image.objects.filter(id=kwargs['image_id']).first()
        access = self.access(image)
        if access:
            form = self.form(request.POST)
            if form.is_valid():
                file_path = image.current.path
                width, height = request.POST.get('width'), request.POST.get('height')
                width = int(width) if width else 0
                height = int(height) if height else 0
                img = resize_image(image, (width, height))
                image.current.save(image.origin.name, img)
                os.remove(file_path)  # удаляем предыдущую версию
        return render(request, 'changer.html', {'form': self.form(), 'image': image, 'access': access})

