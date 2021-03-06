from datetime import datetime, timezone

from todo_list.models import Category, Task
from .serializers import CategorySerializer, FullTaskSerializer, ShortTaskSerializer, UserSerializer
from .permissions import UserPermissionsSet, TaskPermissionsSet, CategoryPermissionsSet

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets

from django.db.models import Q, Prefetch
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from django_currentuser.middleware import get_current_authenticated_user


def secs_to_time(s):
    check = s
    days = s // 86400
    s -= days * 86400
    hours = s // 3600
    s -= hours * 3600
    minutes = s // 60
    s -= minutes * 60
    seconds = s // 1
    if check > 0:
        return str(days) + ' days, ' + \
               str(hours) + ' hours, ' + \
               str(minutes) + ' minutes, ' + \
               str(seconds) + ' seconds'
    return 'Deadline has come ' + \
               str(days) + ' days, ' + \
               str(hours) + ' hours, ' + \
               str(minutes) + ' minutes, ' + \
               str(seconds) + ' seconds ago'


class UserPaginationClass(PageNumberPagination):
    page_size = 2


class TaskPaginationClass(PageNumberPagination):
    page_size = 3


class CategoryPaginationClass(PageNumberPagination):
    page_size = 1


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, UserPermissionsSet, )
    pagination_class = UserPaginationClass

    @action(methods=['get'], detail=True)
    def hello(self, request, pk):
        try:
            user = User.objects.get(pk=pk)    # or id=pk
            d = {'name': user.first_name,
                 'surname': user.last_name,
                 'email': user.email}
            return Response([d, 'Hello, ' + d['name'] + ' ' + d['surname']])
        except User.DoesNotExist as e:    # or except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = FullTaskSerializer
    permission_classes = (permissions.IsAuthenticated, TaskPermissionsSet, )
    pagination_class = TaskPaginationClass

    def get_serializer_class(self):
        user_roots = get_current_authenticated_user().is_superuser    # or user.is_stuff
        if self.action == 'list' and not user_roots:
            return ShortTaskSerializer
        return FullTaskSerializer

    def get_queryset(self):
        user = get_current_authenticated_user()
        user_id = user.id
        user_roots = user.is_superuser    # or user.is_stuff
        if not user_roots:
            return Task.objects.filter(Q(author=user_id) | Q(worker=user_id))
        return Task.objects.all()

    @action(methods=['get'], detail=True)
    def time_left(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)    # or id=pk
            start = datetime.now(timezone.utc)
            end = task.deadline
            time_diff = end - start
            return Response(secs_to_time(int(time_diff.total_seconds())))
        except Task.DoesNotExist as e:    # or except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated, CategoryPermissionsSet, )
    pagination_class = CategoryPaginationClass

    def get_queryset(self):
        user = get_current_authenticated_user()
        user_id = user.id
        user_roots = user.is_superuser    # or user.is_stuff
        if not user_roots:
            return Category.objects.prefetch_related(
                Prefetch('all_tasks', queryset=Task.objects.filter(Q(author=user_id) | Q(worker=user_id)))).all()
        return Category.objects.all()
