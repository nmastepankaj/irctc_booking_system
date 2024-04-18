from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'You are not a verified user'
    def has_permission(self, request, view):
        if request.method == 'GET' or 'POST' or 'PUT' or 'PATCH' or 'DELETE' or 'OPTIONS':
            return request.user.is_staff and request.user.is_active
        return False
