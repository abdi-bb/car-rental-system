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
        # Allow GET requests (viewing) for any user's review
        if request.method in permissions.SAFE_METHODS:
            return True

        # Prevent updates or deletions for other customers' reviews
        return obj.user == request.user
    
    

class AdminCanNotPost(permissions.BasePermission):
    """
    Custom permission to allow only non-admin users to create reviews or bookings.
    Admin users are allowed to update and delete.
    """
    def has_permission(self, request, view):
        # Allow GET requests (viewing) for any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow POST requests (creation) only for non-admin users
        return not request.user or not request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Allow updates and deletes for any user, including admin
        return True
