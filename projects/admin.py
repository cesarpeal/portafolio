from django.contrib import admin
from .models import Project, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


# Register your models here.
admin.site.register(Project)
admin.site.register(Image, ImageAdmin)