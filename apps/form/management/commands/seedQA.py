import json
from django.core.management.base import BaseCommand
from apps.form.models import QuestionModel
from apps.form.serializers import QuestionSerializer, AnswerSerializer
class Command(BaseCommand):

    help = 'seedQA'

    def handle(self, *args, **options):

        file = open('apps/form/management/commands/seedQA.json', encoding="utf8")
        JSdata = json.load(file)
    
        for i in JSdata:
            print(i['question'])
            dataq = {
                'question': i['question']
            }
            Qserial = QuestionSerializer(data=dataq)
            if Qserial.is_valid():
                Qserial.save()
                
                for ans in i['answers']:

                    dataa={
                    'answer': ans['answer'], 
                    'role':ans['role'], 
                    'feel': ans['feel'],
                    'fk_question':Qserial.data['id']}

                    anSerial = AnswerSerializer(data=dataa)
                    if anSerial.is_valid():
                        anSerial.save()
                        
                          
            