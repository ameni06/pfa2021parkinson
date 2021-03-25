from rest_framework import serializers 
from parkinson.models import parkinson
 
 
class parkinsonSerializer(serializers.ModelSerializer):
 
    class Meta:
        model =parkinson
        fields = ('id',
                  'login',
                  'password',
                  'stepsNum')