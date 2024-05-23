from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Дозвіл на доступ тільки для адміністратора.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
