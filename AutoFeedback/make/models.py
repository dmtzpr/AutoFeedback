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


class Generation(models.Model):
    class Meta():
        db_table = 'generation'
    name = models.CharField(max_length = 50)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank = True, null = True)
    model = models.ForeignKey(Model)


class Comment(models.Model):
    class Meta():
        db_table = 'comment'
    author = models.CharField(max_length = 50)
    date = models.DateField(auto_now_add = True)
    likes = models.IntegerField(default = 0)
    text = models.TextField()
    generation = models.ForeignKey(Generation)




