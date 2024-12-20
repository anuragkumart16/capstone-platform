from django.db import models

class QueryModel(models.Model):
    query = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=200)
    file = models.FileField(blank=True,upload_to='uploads/')
    student = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000,null=True,blank=True)
    is_answered = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.query} {self.mentor} {self.student}'

class CapstoneModel(models.Model):
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
    
