from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register('create-question', QuestionSet, name='CreateQ')
router.register('create-answer', AnswerSet, name = 'CreateA')
router.register('', ShowQuestions, name='read')
urlpatterns = [
    ]

urlpatterns += router.urls