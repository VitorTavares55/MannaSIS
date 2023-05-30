from django.contrib import admin
from .models import Status
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Status)

