from .views import TaskViewSet, CategoryViewSet, UserViewSet, UserTasksViewSet
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('state', CategoryViewSet)
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
