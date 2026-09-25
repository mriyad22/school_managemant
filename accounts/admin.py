from django.contrib import admin
from .models import AuthUserModel

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')

admin.site.register(AuthUserModel, UserAdmin)

