from django.db import models

# Create your models here.
class Programming_Authors(models.Model):
    programming_languages = models.CharField(max_length=20)
    authors = models.CharField(max_length=100)
    date_of_birth = models.DateField()  
    def __str__(self):
        return self.authors

class ProgrammingFramework(models.Model):
    framework_name = models.CharField(max_length=40)
    framework_type = models.CharField(max_length=40)
    programming_authors = models.ForeignKey(Programming_Authors,on_delete=models.CASCADE)

    def __str__(self):
        return self.framework_name
