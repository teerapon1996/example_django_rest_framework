from django.db import models

# Create your models here.
from django.db import models
import uuid
# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):                                             
        return self.name

class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    
    def __str__(self):                                             
        return self.firstname
