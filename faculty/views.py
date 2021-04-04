from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from auth_api.permissions import IsCRPAdminUser

from faculty.models import FacultyTakesCourse
from faculty.serializers import FacultyTakesCourseSerializer

# Create your views here.


class FacultyTakesCourseView(generics.ListAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser | IsCRPAdminUser)

    serializer_class = FacultyTakesCourseSerializer
    queryset = FacultyTakesCourse.objects

    def post(self, request):
        serializer = FacultyTakesCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
