from rest_framework import serializers 
from airoapp.models import Tutorial, Message
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')

class MessageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Message
        fields = ('deveui',
                  'timestamp',
                  'payload_ciphered',
                  'payload_deciphered',
                  'data',
                  'lorawan',
                  'lora',
                  'gateway',
                  'gps')