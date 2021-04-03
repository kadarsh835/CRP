from django.db import models

from miscellaneous.models import Department

SEMESTER= (
    ('1', 'First'),
    ('2', 'Second'),
)

# Create your models here.
class Course(models.Model):
    course_code= models.CharField(max_length= 10)
    title= models.CharField(max_length= 50)
    department= models.ForeignKey(Department, on_delete=models.SET_NULL, null= True)
    lectures= models.SmallIntegerField(default= 3)
    tutorials= models.SmallIntegerField(default= 1)
    practicals= models.SmallIntegerField(default= 0)
    self_study= models.DecimalField(max_digits= 2, decimal_places= 1, default= 2)
    course_credits= models.DecimalField(max_digits= 2, decimal_places= 1, default= 3)
    
    def save(self, *args, **kwargs):
        self.course_code= self.course_code.upper()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_code+' '+self.title


class CourseSection(models.Model):
    course= models.ForeignKey(Course, on_delete=models.SET_NULL, null= True)
    semester= models.CharField(max_length=1, choices=SEMESTER)
    year= models.SmallIntegerField()

    def __str__(self):
        return self.course.course_code+ ' '+ str(self.year)+ '(Sem '+ self.semester+ ')'


class PreRequisites(models.Model):
    course= models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    prerequisite= models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prerequisite')

    def __str__(self):
        return self.course.course_code+' '+self.prerequisite.course_code