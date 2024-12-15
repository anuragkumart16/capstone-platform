from django.db import models

class MentorModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class QueryModel(models.Model):
    query = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=200)
    file = models.FileField(blank=True,upload_to='uploads/')
    student = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return f'{self.query} {self.mentor} {self.student}'

class CapstoneModel(models.Model):
    Mentor_Names = [
        ('Rishab Sir', 'Rishab Sir'),
        ('Vishal Sir', 'Vishal Sir'),
        ('Abhiman Sir', 'Abhiman Sir'),
        ('Naman Sir', 'Naman Sir'),
        ('Piyush Sir', 'Piyush Sir'),
        ('Ayush Sir', 'Ayush Sir'),
        ('Divy Sir', 'Divy Sir'),
        ('Adit Sir', 'Adit Sir'),
        ('Param Sir', 'Param Sir'),
    ]
    student = models.CharField(blank=False,max_length=200)
    mentor = models.CharField(blank=False,max_length=200)
    figma_link = models.CharField(max_length=800)

    def __str__(self):
        return f'{self.student} {self.mentor}'

class SubmissionModel(models.Model):
    student = models.EmailField(default=None,unique=True)
    hosted_link = models.CharField(max_length=800,default=None)
    github_link = models.CharField(max_length=800,default=None)
    explanation_link = models.CharField(max_length=800,default=None)

    def __str__(self):
        return self.student
    
class ResultModel(models.Model):
    name = models.CharField(max_length=50,blank=False,unique=True)