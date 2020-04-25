from django.contrib import admin

from miscellaneous import models

# Register your models here.

class DepartmentAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.Department._meta.fields]

admin.site.register(models.Department, DepartmentAdminView)