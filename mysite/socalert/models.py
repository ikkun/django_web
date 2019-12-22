from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ("Net", ("Network/System")),
    ("Ser", ("Services")),
    ("Sec", ("Security")),
)

SEVERITY_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)

ISINCIDENT_CHOICES = (
    (0, 'Unaware'),
    (1, 'Incident'),
    (2, 'Event'),
    
)

class Event_alert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    types= models.CharField(max_length=50, choices=TYPE_CHOICES,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)    
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    contact = models.CharField(max_length=500,null=True,blank=True)
    is_incident = models.IntegerField(choices=ISINCIDENT_CHOICES,default=0)
    ackby = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title