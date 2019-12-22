from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Event_alert

# class Event_alertSerializer(serializers.HyperlinkedModelSerializer):
class Event_alertSerializer(serializers.ModelSerializer):
    
    def create(self,data):
        response = {
                    "message": "Alert exists not allowd!",
                    "success": False,
                    "error": 1
                }
        
        qs = Event_alert.objects.filter(title__iexact=data['title'],ackby_id__isnull=True)
        
        if qs.exists():
            raise serializers.ValidationError(response)       

        return Event_alert.objects.create(**data)  

    class Meta:
        model = Event_alert
        fields = ('types','title','description','severity','contact')

    