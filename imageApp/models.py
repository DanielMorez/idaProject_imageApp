from django.db import models
from django.urls import reverse


class Customer(models.Model):
    remote_addr = models.GenericIPAddressField(verbose_name='IP-адрес пользователя', null=False)
    csrf_token = models.CharField(max_length=50, verbose_name='CSRF-TOKEN', null=False)

    def __str__(self):
        return f"[id:{self.id}] {self.remote_addr}:{self.csrf_token}"


class Image(models.Model):
    title = models.CharField(max_length=124, verbose_name='Название изображения')
    owner = models.ForeignKey(Customer, verbose_name='Владелец изображения', on_delete=models.CASCADE)
    origin = models.ImageField(verbose_name='Оригинал изображения')
    current = models.ImageField(verbose_name='Изображение')

    def __str__(self):
        return f"[id:{self.id}] image of {self.owner.remote_addr}"

    def absolute_url(self):
        return reverse('changer', kwargs={'image_id': self.id})
