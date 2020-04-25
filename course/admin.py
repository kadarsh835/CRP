from django.contrib import admin

from course import models

# Register your models here.

class CourseAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.Course._meta.fields]

admin.site.register(models.Course, CourseAdminView)

class CourseSectionAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.CourseSection._meta.fields]

admin.site.register(models.CourseSection, CourseSectionAdminView)

class PrerequisitesAdminView(admin.ModelAdmin):
    list_display= [field.name for field in models.PreRequisites._meta.fields]

admin.site.register(models.PreRequisites, PrerequisitesAdminView)