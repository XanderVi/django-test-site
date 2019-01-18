from django.contrib import admin
from django.urls import include, path

from . import views


app_name = 'todo_list'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]