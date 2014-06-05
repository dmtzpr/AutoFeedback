from django.db import models

# Create your models here.

class Make(models.Model):
    class Meta():
        db_table = 'make'
    name = models.CharField(max_length = 50)
    logo = models.CharField(max_length = 200)
    description = models.TextField()

class Model(models.Model):
    class Meta():
        db_table = 'model'
    name = models.CharField(max_length = 50)
    description = models.TextField()
    make = models.ForeignKey(Make)
