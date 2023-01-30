from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination
from .serializers import QuestionSerializer, AnswerSerializer
from .models import QuestionModel, AnswerModel

def index(request):

    return render(request,'index.html')

def question(request):
    
    return render(request, 'quizz.html')

class QuestionSet(GenericViewSet, CreateModelMixin):

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class AnswerSet(GenericViewSet, CreateModelMixin):

    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

class ShowQuestions(ReadOnlyModelViewSet):
    
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer