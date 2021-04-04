from django.db import models
from django.contrib.auth.models import User

from course.models import Course, CourseSection
from miscellaneous.models import Department

SEMESTER = (
    (1, 'First'),
    (2, 'Second'),
)


class Faculty(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.__str__()


class FacultyTakesCourse(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(
        CourseSection, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.section.course.course_code+' ' + \
            str(self.section.year)+' Sem: ' + self.section.semester
