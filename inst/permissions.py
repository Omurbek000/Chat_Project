from rest_framework import permissions

class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view): # type: ignore
        if request.user.role == 'teacher':
            return True
        return False


class CheckUserOwner(permissions.BasePermission):
    def has_permission(self, request, view): # type: ignore
        if request.user.role =='student':
            return True
        return False


class CheckCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): # type: ignore
        if obj.teacher.id == request.user.id:
            return True
        return False