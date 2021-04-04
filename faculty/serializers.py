from rest_framework import serializers

from faculty.models import Faculty, FacultyTakesCourse
from course.models import Course, CourseSection

from course.serializers import CourseSectionSerializer


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('__all__')


class FacultyTakesCourseSerializer(serializers.ModelSerializer):

    faculty = FacultySerializer()
    section = CourseSectionSerializer()

    class Meta:
        model = FacultyTakesCourse
        fields = ['id', 'faculty', 'section']

    def create(self, validated_data):

        faculty = Faculty.objects.create(**validated_data['faculty'])
        course = Course.objects.create(**validated_data['section']['course'])

        section = CourseSection.objects.create(course=course,
                                               semester=validated_data['section']['semester'], year=validated_data['section']['year'])

        return FacultyTakesCourse.objects.create(faculty=faculty, section=section)
