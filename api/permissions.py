from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the tags owner."""
        return obj.owner == request.user
