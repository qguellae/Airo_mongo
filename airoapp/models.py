from django.db import models
import mongoengine as me

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Message(models.Model):
    deveui=models.CharField(max_length=70, blank=False, default='') #"fcd6bd0000192c22",
    timestamp=models.CharField(max_length=70, default='')# "2020-02-10T09:28:48.064918Z",
    payload_ciphered=models.CharField(max_length=70, default='')# "6543210fedcba",
    payload_deciphered=models.CharField(max_length=70, default='')#4c4000f930",
    data=me.DictField(default='')#{"2.5":10.2, "10":15.5}
    lorawan=me.DictField(default='')#{"type": "unconfirmed_data_up", "devaddr": "abcdef01", "adr": true, "fcnt": 1234, "port": 1 },
    lora=me.DictField(default='')#{"freq": 868.5, "data_rate": "SF7BW125", "rssi": -52,"lsnr": -1.5 },
    gateway=me.DictField(default='')#{"best": "ABCDEF0123456789", "number": 1234 },
    gps=me.DictField(default='')#{"lat": 48.6,"lng": -1.6}