from .views import PollAPIView
from django.conf.urls import url
from django.urls import path


urlpatterns = [
    path('', PollAPIView.as_view()),
    path('<int:pk>', PollAPIView.as_view()),
]