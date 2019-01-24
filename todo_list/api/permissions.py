from rest_framework import permissions


class UserPermissionsSet(permissions.BasePermission):
    message = 'Something go wrong...'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.has_perm('todo_list.add_user')
        elif request.method == 'DELETE':
            return request.user.has_perm('todo_list.delete_user')
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('todo_list.change_user')
        return True


class TaskPermissionsSet(permissions.BasePermission):
    message = 'Something go wrong...'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.has_perm('todo_list.create_a_task')
        elif request.method == 'DELETE':
            return request.user.has_perm('todo_list.delete_a_task')
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('todo_list.change_a_task')
        return True


class CategoryPermissionsSet(permissions.BasePermission):
    message = 'Something go wrong...'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.has_perm('todo_list.create_new_category')
        elif request.method == 'DELETE':
            return request.user.has_perm('todo_list.delete_a_category')
        elif request.method == 'PUT' or request.method == 'PATCH':
            return request.user.has_perm('todo_list.change_a_category')
        return True
