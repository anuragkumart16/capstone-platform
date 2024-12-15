from django.db import models

# Create your models here.

class MentorModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class MarksModel(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField( max_length=254)
    html_structure = models.IntegerField()
    css_design = models.IntegerField()
    responsiveness = models.IntegerField()
    functional_design = models.IntegerField()
    debugging = models.IntegerField()

    def __str__(self):
        return f' {self.name} {self.email} {self.html_structure + self.css_design + self.responsiveness + self.functional_design + self.debugging}'