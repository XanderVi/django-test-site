from rest_framework import serializers

from todo_list.models import Category, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(source='all_tasks', many=True)
    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['pk']

