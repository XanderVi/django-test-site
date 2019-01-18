from django.db.models import Q
from rest_framework import generics, mixins
from todo_list.models import Category, Task
from .serializers import CategorySerializer


class TodoAPIView(mixins.CreateModelMixin,
                  generics.ListAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(question_text__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

