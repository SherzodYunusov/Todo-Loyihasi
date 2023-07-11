from rest_framework import serializers
from .models import *


class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=50)
    davlat = serializers.CharField(max_length=50)
    jins = serializers.CharField(max_length=50)
    tugulgan_yil = serializers.DateField()
    def validate_ism(self, qiymat):
        if len(qiymat) < 3:
            raise serializers.ValidationError("ism bunday bolishi mumkun emas!")
        return qiymat

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = ('id','matn','user','sana','baho', 'kino')

    def validate_baho(self, qiymat):
        if qiymat >= 5 or qiymat <= 1:
            raise serializers.ValidationError("Baholash faqatgina 1 bilan 5 oraligida bolish kerak!")
        return qiymat

    def validate_matn(self, qiymat):
        lst = ['Yomon', 'Ortacha', 'Oxshamapti']
        for i in lst:
            if qiymat == i:
                raise serializers.ValidationError("Bunday izoh kiritish mumkun emas!")
            return qiymat

class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True)
    class Meta:
        model = Kino
        fields = '__all__'

class KinoSaqlashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kino
        fields = '__all__'

