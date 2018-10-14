from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated'
    """
    Non-authenticated Users only.
    """
    def has_permission(self, request, view):
        return not request.user.is_authenticated