from django.db.models import Q
from rest_framework import generics, mixins, status
from todo_list.models import Category, Task
from .serializers import CategorySerializer, TaskSerializer, UserSerializer, UserTasksSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django_currentuser.middleware import get_current_authenticated_user
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def hello(self, request, pk):
        try:
            user = User.objects.get(pk=pk)    #or id=pk
            d = {'name': user.first_name, 'email': user.email}
            return Response(d)
        except User.DoesNotExist as e:    #or except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('deadline')
    serializer_class = TaskSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class UserTasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('deadline')
    serializer_class = UserTasksSerializer


