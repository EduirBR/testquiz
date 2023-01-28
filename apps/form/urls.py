from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter(trailing_slash=False)
router.register('ALL', ShowQuestionsALL)
router.register('create-question', QuestionSet)
router.register('create-answer', AnswerSet)
router.register('', ShowQuestions)
urlpatterns = [
    ]

urlpatterns += router.urls