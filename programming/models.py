from django.db import models

# Create your models here.
class Programming_Authors(models.Model):
    programming_languages = models.CharField(max_length=20)
    authors = models.CharField(max_length=100)
    date_of_birth = models.DateField()  
    def __str__(self):
        return self.authors