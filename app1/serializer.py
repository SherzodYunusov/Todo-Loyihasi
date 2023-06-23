from rest_framework import serializers
from .models import *



class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    davlat = serializers.CharField(max_length=50)
    jins = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = ('id','matn','user','sana','baho', 'kino')

    # id = serializers.IntegerField(read_only=True)
    # matn = serializers.CharField(max_length=1000)
    # sana = serializers.DateField()
    # baho = serializers.IntegerField()


