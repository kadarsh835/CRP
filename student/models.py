from django.db import models
from django.contrib.auth.models import User

from miscellaneous.models import Department
from course.models import Course, CourseSection

SEMESTER= (
    (1, 'First'),
    (2, 'Second'),
)

# Create your models here.
class Student(models.Model):
    user= models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    entry_number= models.CharField(max_length=20)
    department= models.ForeignKey(Department, on_delete=models.SET_NULL, null= True)

    def save(self, *args, **kwargs):
        self.entry_number= self.entry_number.upper()
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.__str__()


class StudentTakesCourse(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    section_id= models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null= True)
    course_id= models.ForeignKey(Course, on_delete=models.SET_NULL, null= True)
    semester= models.CharField(max_length=1, choices=SEMESTER)
    year= models.SmallIntegerField()
    grade= models.SmallIntegerField(default=0)

    def __str__(self):
        return self.student.user.__str__()+' '+self.course_id.__str__()+' '+str(self.year)+' '+self.semester