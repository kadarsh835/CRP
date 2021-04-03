from django.contrib import admin

from admin_user import models

# Register your models here.

class AdminUserAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.AdminUser._meta.fields]

admin.site.register(models.AdminUser, AdminUserAdminView)