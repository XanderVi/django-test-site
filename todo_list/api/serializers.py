from rest_framework import serializers
from todo_list.models import Category, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'author', 'worker', 'first_name')
        #depth = 0


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(source='all_tasks', many=True)

    class Meta:
        model = Category
        fields = '__all__'


class UserTasksSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(source='all_tasks', many=True)

    class Meta:
        model = User
        fields = ('url', 'id')
