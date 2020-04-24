from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.hospitals.models import HospitalUser

class HospitalUserInline(admin.StackedInline):
    model = HospitalUser
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (HospitalUserInline,)

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)