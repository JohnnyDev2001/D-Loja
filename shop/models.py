from email.mime import image
from django.db import models
import datetime
import os

def getFileName(request, filename):
    now_time=datetime.datetime.now().strftime("%d%m%Y%H:%M:%S")
    new_filename='%s%s'%(now_time, filename)
    return os.path.join('uploads/', new_filename)

class Menu(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=False)
    description=models.TextField(max_length=500, null=False, blank=False)
    vote = models.CharField(max_length=10)
    show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MenuBar(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=getFileName, null=True, blank=False)
    description=models.TextField(max_length=500, null=False, blank=False)
    vote = models.CharField(max_length=10)
    show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name