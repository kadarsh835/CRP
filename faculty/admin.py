from django.contrib import admin

from faculty import models

# Register your models here.

class FacultyAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.Faculty._meta.fields]

admin.site.register(models.Faculty, FacultyAdminView)

class FacultyTakesCourseAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.FacultyTakesCourse._meta.fields]

admin.site.register(models.FacultyTakesCourse, FacultyTakesCourseAdminView)