from rest_framework import permissions
from admin_user.models import AdminUser


class IsCRPAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        try:
            admin_user = AdminUser.objects.get(user=request.user)
            return True
        except:
            return False
