from django.db import models
from django.contrib.auth.models import User

class Test(models.Model):
    
    STATUS_TYPES = (
        ('Not published','Not published'),
        ('Published','Published'),
    )
    
    author = models.ForeignKey(User,related_name='author')
    name = models.CharField('name',max_length=100)
    description = models.TextField('description')
    status = models.CharField('status',choices=STATUS_TYPES,default=STATUS_TYPES[0][0],max_length=100)
    created_date = models.DateField('created date',auto_now_add=True)
    modified_date = models.DateField('modified date',auto_now=True)
    
    def __unicode__(self):
        return self.name
