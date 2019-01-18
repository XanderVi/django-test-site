from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, path
from .models import Category, Task
from django.views import generic
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer

from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer

#SOCIAL AUTH & CONNECTION

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter

#TASKS VIEWS

def home(request):
    return render(request, 'todo_list/main.html')

class IndexView(generic.ListView):
    template_name = 'todo_list/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all tasks."""
        return Task.objects.order_by('deadline')


class DetailView(generic.DetailView):
    model = Task
    template_name = 'todo_list/detail.html'


schema_view = get_swagger_view(title='Test Swagger')