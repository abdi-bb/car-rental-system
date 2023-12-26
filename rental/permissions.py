from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        return bool(request.user and request.user.is_staff)
        # return super().has_permission(request, view)
        

class CanModifyOwnReview(permissions.BasePermission):
    """
    Custom permission to allow viewing, but not updating or deleting,
    other customers' reviews.
    """
    def has_object_permission(self, request, view, obj):
        # Allow GET requests (viewing) for any customer's review
        if request.method in permissions.SAFE_METHODS:
            return True

        # Prevent updates or deletions for other customers' reviews
        return obj.customer == request.user.customer
    
    
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