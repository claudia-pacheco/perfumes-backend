from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
       # Authenticated users only can see list view
        if request.user and request.user.is_authenticated:
            return True
        return False

    # Authorization
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """

        # POST
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.createdBy == request.user


class IsSafeMethod(permissions.BasePermission):
    message = 'Only save http methods allowed'

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsPutOrGetMethod(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method == 'PUT' or request.method == 'GET'


class IsCreator(permissions.BasePermission):
    message = 'You have to be the creator in order to amend this fragrance'

    def has_object_permission(self, request, view, obj):
        return obj.createdBy == request.user
