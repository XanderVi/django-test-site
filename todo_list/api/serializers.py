from rest_framework import serializers
from todo_list.models import Category, Task
from django.contrib.auth.models import User


class ShortTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'category', 'title', 'author', 'worker')


class FullTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email')
        depth = 1


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    tasks = ShortTaskSerializer(source='all_tasks', many=True)

    class Meta:
        model = Category
        fields = '__all__'
