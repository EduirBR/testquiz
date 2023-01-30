from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register('create-question', QuestionSet)
router.register('create-answer', AnswerSet)
router.register('question', ShowQuestions)
urlpatterns = [
    path('', index, name='home'),
    path('quizz', question, name='quizz')
    ]

urlpatterns += router.urls