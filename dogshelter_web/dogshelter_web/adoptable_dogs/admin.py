from django.contrib import admin
from .models import Dog, DogImages

class DogImagesInline(admin.TabularInline):
    model = DogImages

class DogAdmin(admin.ModelAdmin):
    inlines = [
        DogImagesInline,
    ]

admin.site.register(Dog, DogAdmin)