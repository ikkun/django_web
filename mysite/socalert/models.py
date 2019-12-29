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

IMPACT_CHOICES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Medium'),
    (4, 'Low')
)

URGENCY_CHOICES = (
    (1, 'Critical'),
    (2, 'High'),
    (3, 'Medium'),
    (4, 'Low')
)

class Event_alert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    types= models.CharField(max_length=50, choices=TYPE_CHOICES,null=True,blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)    
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    contact = models.CharField(max_length=500,null=True,blank=True)
    is_incident = models.IntegerField(choices=ISINCIDENT_CHOICES,default=0)
    analyse_by = models.ForeignKey(User,null=True,blank=True,related_name='analyst2user',on_delete=models.SET_NULL)
    analyse_at = models.DateTimeField(null=True,blank=True)
    is_closed = models.IntegerField(default=0)
    closed_by = models.ForeignKey(User,null=True,blank=True,related_name='closedby2user',on_delete=models.SET_NULL)
    closed_at = models.DateTimeField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

class Event_rule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    types= models.CharField(max_length=50, choices=TYPE_CHOICES,null=True,blank=True)
    rule = models.CharField(max_length=10 , unique=True)
    service = models.CharField(max_length=100,null=True,blank=True)
    title = models.CharField(max_length=255)
    impact = models.IntegerField(choices=IMPACT_CHOICES)
    urgency = models.IntegerField(choices=URGENCY_CHOICES)
    contact = models.TextField(null=True,blank=True)
    howto = models.TextField(null=True,blank=True)
    created_by =models.ForeignKey(User,null=True,blank=True,related_name='createdby2user',on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(null=True,blank=True)
    updated_by = models.ForeignKey(User,null=True,blank=True,related_name='updatedby2user',on_delete=models.SET_NULL)

    def __str__(self):
        return self.rule