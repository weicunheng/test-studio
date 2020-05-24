from django.contrib import admin
from studioapps.account.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('real_name',)
