from rest_framework import permissions


class AdminCanModifyAnyView(permissions.BasePermission):
    """
    Custom permission class to allow only admin users to modify any view.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.is_staff and 
            request.method in ["GET", "PUT", "PATCH", "DELETE"]
        )