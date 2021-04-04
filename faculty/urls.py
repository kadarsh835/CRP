from django.urls import path, include
from django.conf.urls import url

from faculty.views import FacultyTakesCourseView

urlpatterns = [
    path('faculty-courses/', FacultyTakesCourseView.as_view()),
]
