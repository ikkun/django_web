from rest_framework import serializers
from .models import ScanSchedule

class ScanTasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ScanSchedule
        fields=('id','url','appname','taskscan')