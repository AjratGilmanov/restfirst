from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.IntegerField()
    autor = models.CharField(max_length=50)
    year = models.IntegerField()


    def __str__(self):
        return self.name

# class Task(models.Model):
#   title = models.CharField(max_length=200)
#   completed = models.BooleanField(default=False, blank= True, null= True)

#   def __str__(self):
#     return self.title
