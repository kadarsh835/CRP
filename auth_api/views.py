from django.shortcuts import render

# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from django.contrib.auth.models import User
from student.models import Student
from miscellaneous.models import Department

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

def createStudents(csv_file):
    for row in csv_file:
        user= User.objects.create(email= row['Email'], first_name= row['First Name'], last_name= row['Last Name'], username= row['Email'])
        department = Department.objects.filter(name='CSE')[0]
        Student.objects.create(user=user, entry_number= row['Entry Number'], department= department)
    
    return