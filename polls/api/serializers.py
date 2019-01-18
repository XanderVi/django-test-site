from rest_framework import serializers

from polls.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = ChoiceSerializer(source='all_answers', many=True)
    
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ['pk']

    def validate_quest(self, value):
        qs = Question.objects.filter(question_text__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('The question should be unique')
        return value

