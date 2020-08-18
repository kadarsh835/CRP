from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from auth_api.views import GoogleLogin
from auth_api import api

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    path('upload-csv/', api.UploadCSV.as_view()),
]