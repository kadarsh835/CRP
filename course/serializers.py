from rest_framework import serializers

from course.models import Course, CourseSection


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('__all__')


class CourseSectionSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = CourseSection
        fields = ('__all__')
