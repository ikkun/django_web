from django.db import models

class ScanSchedule(models.Model):
    appname = models.CharField(max_length=100,unique=True)
    taskscan = models.CharField(max_length=150)
    dtmodified = models.DateTimeField(auto_now_add=True)
