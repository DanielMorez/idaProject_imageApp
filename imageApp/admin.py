from django.contrib import admin

from .models import Image, Customer


@admin.register(Image)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('origin',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('remote_addr', 'csrf_token')
