from django.contrib import admin
from studioapps.project.models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'creator')
    search_fields = ('name', 'code',)


@admin.register(AppTags)
class AppTagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code',)


@admin.register(ProjectMembers)
class ProjectMembersAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'permissionType',)
    search_fields = ('project', 'name', 'permissionType',)
