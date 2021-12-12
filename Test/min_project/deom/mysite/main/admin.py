from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')


admin.site.register(Tutorial, TutorialAdmin)