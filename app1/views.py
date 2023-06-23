from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *

class HelloApiView(APIView):
    def get(self, request):
        d = {
            "xabar": "Hello World",
            "sana":"22.06.2023"
        }
        return Response(d)

    def post(self, request):
        malumot = request.data
        d = {
            "xabar": "POST qabul qilindi",
            "post_malumoti": malumot
        }
        return Response(d)

class AktyorApiView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        x = AktyorSerializer(aktyorlar, many=True)
        return Response(x.data)

    def post(self, request):
        malumot = request.data
        serializer = AktyorSerializer(data=malumot)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get('ism'),
                davlat = serializer.validated_data.get('davlat'),
                tugulgan_yil = serializer.validated_data.get('tugulgan_yil'),
                jins = serializer.validated_data.get('jins'),
            )
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BittaAktyorApiView(APIView):
    def get(self, request, pk):
        aktyorlar = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyorlar)
        return Response(serializer.data)

class OchirishAktyorApiView(APIView):
    def delete(self, request, pk):
        aktyor = Aktyor.objects.filter(id=pk).delete()
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)

class IzohApiView(APIView):
    def get(self, request):
        izohlar = Izoh.objects.all()
        x = IzohSerializer(izohlar, many=True)
        return Response(x.data)

    def post(self, request):
        malumot = request.data
        serializers = IzohSerializer(data=malumot)
        if serializers.is_valid():
            Izoh.objects.create(
                matn = serializers.validated_data.get('matn'),
                sana = serializers.validated_data.get('sana'),
                baho = serializers.validated_data.get('baho'),
                kino = serializers.validated_data.get('kino'),
                user = serializers.validated_data.get('user'),
            )
            return Response(serializers.validated_data)
        return Response(serializers.errors)

class BittaIzohApiView(APIView):
    def get(self, request, pk):
        izohlar = Izoh.objects.get(id=pk)
        x = IzohSerializer(izohlar)
        return Response(x.data)




# Create your views here.
