from django.contrib import admin
from django.urls import path

from .views import MainPageView, UploadImageView

urlpatterns = [
    path('', MainPageView.as_view(), name='base'),
    path('upload/', UploadImageView.as_view(), name='upload')
]
