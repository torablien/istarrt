from __future__ import unicode_literals

from django.db import models

# Create your models here.
class projects(models.Model):
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200)
    images = models.CharField(max_length=500)
    video = models.CharField(max_length=200)
    words = models.TextField(max_length = 1000)
    
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
    

