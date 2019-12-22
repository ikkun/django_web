from django import forms
from .models import Event_alert

class Ack_Is_Incident(forms.ModelForm):
    class Meta:
        model = Event_alert
        fields = ['is_incident']