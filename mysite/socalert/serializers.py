from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Event_alert,Event_rule

# class Event_alertSerializer(serializers.HyperlinkedModelSerializer):
class Event_alertSerializer(serializers.ModelSerializer):
    
    def create(self,data):
        response = {
                    "message": "Alert exists not allowd!",
                    "success": False,
                    "error": 1
                }
        
        qs = Event_alert.objects.filter(title__iexact=data['title'],closed_by_id__isnull=True)
        
        if qs.exists():
            raise serializers.ValidationError(response)       

        return Event_alert.objects.create(**data)  

    class Meta:
        model = Event_alert
        fields = ('types','title','description','severity','contact')

class Event_ruleSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Event_rule
        fields = ('rule','types','title','impact','urgency','contact')


    