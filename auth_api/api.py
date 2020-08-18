from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

from auth_api.views import createStudents

import csv

class UploadCSV(APIView):
    authentication_classes= [authentication.TokenAuthentication]
    permission_classes= [permissions.IsAuthenticated]
    
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):

        if 'csv' not in request.data:
            raise ParseError("Empty content")

        csv_file = request.data['csv']
        str_file_value = csv_file.read().decode('utf-8')
        csv_file = str_file_value.splitlines()
        csv_file = csv.DictReader(csv_file)

        createStudents(csv_file)

        return Response(status= status.HTTP_200_OK)
