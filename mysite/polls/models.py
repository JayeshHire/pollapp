from django.db import models

# Create your models here.
def raise_exe():
    try :
        raise ValueError
    finally:
        print("Either you have passed parameters other than\n1. text\n2.msq\n3.mcq\n\
        -----OR-----\nYour parameter type is wrong\n It should be of type string.")
class text:
        pass
class msq:
     pass
class mcq:
      pass        
class question_type:
    
    def __init__(self, _type):
        self.type = _type
        if _type == 'text':
            self.obj = text()
        elif _type == 'msq':
            self.obj = msq()
        elif _type == 'mcq':
            self.obj == mcq()
        else :
            raise_exe()
    
    def __str__(self):
        return self.type

''' 
class QuestionTypeField(models.Field):
    a : str
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

    def create(self,_type):
        obj = question_type(_type)
        self.a = str(obj)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        return name, path, args, kwargs
'''
        
class Question(models.Model):
    text = 'txt'
    mcq = 'mcq'
    msq = 'msq'
    type_choices = [
        (text,"text"),
        (mcq, "multiple choice question"),
        (msq,"multiple select question"),
    ]
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now= True)
    id = models.IntegerField(primary_key=True,auto_created=True)
    type = models.CharField(choices=type_choices,max_length=3,default="mcq")
    
    '''def is_upperclass(self):
        return self.type in {self.text, self.mcq, self.msq}
    '''
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField("correct answer to question",max_length=90)

    def __str__(self):
        return self.answer_text    
