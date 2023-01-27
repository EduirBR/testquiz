from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin
from .serializers import QuestionSerializer, AnswerSerializer
from .models import QuestionModel, AnswerModel

class QuestionSet(GenericViewSet, CreateModelMixin):

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class AnswerSet(GenericViewSet, CreateModelMixin):

    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

class ShowQuestions(ReadOnlyModelViewSet):
    
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
