from django.db import models
from django.contrib.auth.models import User

from course.models import Course, CourseSection
from miscellaneous.models import Department

SEMESTER= (
    (1, 'First'),
    (2, 'Second'),
)


class Faculty(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    department= models.ForeignKey(Department, on_delete= models.SET_NULL, null= True)

    def __str__(self):
        return self.user.__str__()


class FacultyTakesCourse(models.Model):
    faculty= models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    course= models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    section= models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True)
    semester= models.CharField(max_length=1, choices=SEMESTER)
    year= models.SmallIntegerField()

    def __str__(self):
        self.course.code+' '+str(self.year)+' Sem: '+self.semester