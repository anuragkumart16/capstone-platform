from django.db import models

# Create your models here.

class MentorModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name