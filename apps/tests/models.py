from django.db import models
from django.contrib.auth.models import User

import datetime

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


from apps.mptt.models import MPTTModel, TreeForeignKey

class Comment(MPTTModel):
    """ Threaded comments for blog posts """
    test = models.ForeignKey(Test, related_name='comment_test')
    author = models.CharField(max_length=60)
    comment = models.TextField()
    added  = models.DateTimeField(default=datetime.datetime.now())
    # a link to comment that is being replied, if one exists
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        # comments on one level will be ordered by date of creation
        order_insertion_by=['added']