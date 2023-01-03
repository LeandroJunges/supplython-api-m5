from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Employee


class isAdmin(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Employee
    ) -> bool:

        if request.user.is_authenticated and request.user.is_manager:

            return True

        return False
