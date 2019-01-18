from .views import TodoAPIView
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('', TodoAPIView.as_view()),
    path('<int:pk>', TodoAPIView.as_view()),
]