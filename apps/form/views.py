from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination
from .serializers import QuestionSerializer, AnswerSerializer
from .models import QuestionModel, AnswerModel

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class QuestionSet(GenericViewSet, CreateModelMixin):

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

class AnswerSet(GenericViewSet, CreateModelMixin):

    queryset = AnswerModel.objects.all()
    serializer_class = AnswerSerializer

class ShowQuestions(ReadOnlyModelViewSet):
    
    pagination_class = StandardResultsSetPagination

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class ShowQuestionsALL(GenericViewSet, ListModelMixin):
    
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
