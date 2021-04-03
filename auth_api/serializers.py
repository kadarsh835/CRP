from rest_auth import serializers as auth_serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from faculty.models import Faculty
from admin_user.models import AdminUser

class UserDetailsSerializer(auth_serializers.UserDetailsSerializer):
    
    role= serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name', 'role')
        read_only_fields = ('username', )

    def get_role(self, obj):
        try:
            admin_user= AdminUser.objects.get(user= obj)
            return 'admin'
        except:
            try:
                faculty= Faculty.objects.get(user= obj)
                return 'faculty'
            except Exception as e:
                print(e)
                return 'student'
            