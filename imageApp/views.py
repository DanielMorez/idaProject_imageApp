from django.shortcuts import render
from django.views.generic import View

from .models import Image
from .mixin import DetectedCustomerMixin
from .forms import ImageForm


class MainPageView(DetectedCustomerMixin):

    def get(self, request, *args, **kwargs):
        context = {
            'customer': self.owner,
            'images': Image.objects.filter(owner=self.owner)
        }
        return render(request, 'base.html', context)

class UploadImageView(DetectedCustomerMixin):

    def get(self, request, *args, **kwargs):
        return render(request, 'upload.html')

    def post(self, request, *args, **kwargs):
        form = ImageForm(request.POST or None)
        if form.is_valid():

            return render(request, 'upload.html')
        else:
            return render(request, 'upload.html')
