from django.db import models
from apps.tests.models import Test

class Question(models.Model):
    test = models.ForeignKey(Test,related_name='test')
    text = models.TextField('text')
    created_date = models.DateField('created date',auto_now_add=True)
    modified_date = models.DateField('modified date',auto_now=True)
    
    def __unicode__(self):
        return self.text
    
class Answer(models.Model):
    question = models.ForeignKey(Question,related_name='question')
    text = models.CharField('text',max_length=200)
    is_answer = models.BooleanField('is answer')
    created_date = models.DateField('created date',auto_now_add=True)
    modified_date = models.DateField('modified date',auto_now=True)
    
    def __unicode__(self):
        return self.text
