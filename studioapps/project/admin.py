from django.contrib import admin
from studioapps.project.models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'creator')
    search_fields = ('name', 'code',)
