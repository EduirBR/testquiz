from rest_framework.serializers import ModelSerializer
from .models import *

class AnswerSerializer(ModelSerializer):

    class Meta:
        model = AnswerModel
        exclude = ['fk_question',]

class QuestionSerializer(ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = ('id','question', 'answers')