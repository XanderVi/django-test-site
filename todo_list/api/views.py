from rest_framework import status
from todo_list.models import Category, Task
from .serializers import CategorySerializer, FullTaskSerializer, ShortTaskSerializer, UserSerializer, UserTasksSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Q
from django_currentuser.middleware import get_current_authenticated_user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @action(methods=['get'], detail=True)
    def hello(self, request, pk):
        try:
            user = User.objects.get(pk=pk)    # or id=pk
            d = {'name': user.first_name,
                 'surname': user.last_name,
                 'email': user.email}
            return Response(d)
        except User.DoesNotExist as e:    # or except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = FullTaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ShortTaskSerializer
        return FullTaskSerializer

    def get_queryset(self):
        user = get_current_authenticated_user().id
        return Task.objects.filter(Q(author=user) | Q(worker=user))


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserTasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('deadline')
    serializer_class = UserTasksSerializer
