from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        return bool(request.user and request.user.is_staff)
        # return super().has_permission(request, view)
        

class CanViewReviewDetail(permissions.BasePermission):
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