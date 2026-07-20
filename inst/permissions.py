from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Только учителя."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Teacher'


class IsStudent(permissions.BasePermission):
    """Только студенты."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Client'


class IsCourseOwner(permissions.BasePermission):
    """Учитель может редактировать только свой курс."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by.teacher == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Владелец — полный доступ, остальные — только чтение."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'author'):
            return obj.author == request.user
        return False