from django.contrib import admin

from student import models

# Register your models here.

class StudentAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.Student._meta.fields]

admin.site.register(models.Student, StudentAdminView)

class StudentTakesCourseAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.StudentTakesCourse._meta.fields]

admin.site.register(models.StudentTakesCourse, StudentTakesCourseAdminView)