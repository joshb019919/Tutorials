from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Profile only viewed or changed by creating user."""
    def has_object_permission(self, request, view, obj):
        # Ensure user trying to access is indeed owner
        return obj.owner == request.user