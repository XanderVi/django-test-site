from rest_framework import serializers
from todo_list.models import Category, Task
from django.contrib.auth.models import User


class ShortTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'title', 'category')


class FullTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    author = ShortTaskSerializer(many=True)
    worker = ShortTaskSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'author', 'worker', 'first_name', 'last_name', 'email')
        depth = 1


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tasks = ShortTaskSerializer(source='all_tasks', many=True)

    class Meta:
        model = Category
        fields = '__all__'


class UserTasksSerializer(serializers.HyperlinkedModelSerializer):
    tasks = ShortTaskSerializer(source='all_tasks', many=True)

    class Meta:
        model = User
        fields = ('url', 'id')
