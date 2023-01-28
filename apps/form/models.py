from django.db import models

class QuestionModel(models.Model):
    
    question = models.CharField(max_length=100, unique=True)

class AnswerModel(models.Model):

    answer = models.CharField(max_length=100)
    role = models.IntegerField()
    feel = models.IntegerField()
    fk_question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name="answers" )
