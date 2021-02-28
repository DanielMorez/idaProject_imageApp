from django.views.generic import View

from .models import Customer


class DetectedCustomerMixin(View):

    def dispatch(self, request, *args, **kwargs):

        self.owner, created = Customer.objects.get_or_create(
            csrf_token=request.COOKIES['csrftoken'],
            remote_addr=request.META['REMOTE_ADDR'],
        )
        return super().dispatch(request, *args, **kwargs)