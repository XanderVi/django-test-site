from django.db.models import Q
from rest_framework import generics, mixins
from polls.models import Question, Choice
from .serializers import QuestionSerializer


class PollAPIView(mixins.CreateModelMixin,
                  generics.ListAPIView,
                  generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = QuestionSerializer

    def get_queryset(self):
        qs = Question.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(question_text__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

