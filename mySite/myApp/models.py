from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=256)
    abbrev = models.CharField(max_length=64)

    def __str__(self):
        return f"NAME: {self.name}, ABBREV: {self.abbrev}"
    
class Teacher(models.Model):
    title = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    age = models.IntegerField()

    def __str__(self):
        return f"Title: {self.title}, Name: {self.name}, Surname: {self.surname}, Age: {self.age}"