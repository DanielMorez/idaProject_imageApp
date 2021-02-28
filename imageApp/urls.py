from django.contrib import admin
from django.urls import path

from .views import MainPageView, UploadImageView, ChangeImageSizeView

urlpatterns = [
    path('', MainPageView.as_view(), name='base'),
    path('upload/', UploadImageView.as_view(), name='upload'),
    path('change/<int:image_id>/', ChangeImageSizeView.as_view(), name='changer')
]
