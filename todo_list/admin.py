from django.contrib import admin

from .models import Category, Task


class TaskInline(admin.StackedInline): #or TabularInline
    model = Task
    extra = 1

class CategoryTasksAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(Category, CategoryTasksAdmin)