from django.contrib import admin
from .models import Gallery, News, Story, StoryImages

class StoryImagesInline(admin.TabularInline):
    model = StoryImages

class StoryAdmin(admin.ModelAdmin):
    inlines = [
        StoryImagesInline,
    ]

admin.site.register(Story, StoryAdmin)
admin.site.register(Gallery)
admin.site.register(News)