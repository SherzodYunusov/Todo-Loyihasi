from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.postgres.search import TrigramSimilarity

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import *

from .models import *
from .serializer import *

class HelloApiView(APIView):
    def get(self, request):
        d = {
            "xabar": "Hello World",
            "sana": "22.06.2023"
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
        soz = request.query_params.get('qidiruv')
        if soz:
            aktyorlar = Aktyor.objects.annotate(oxshashlik=TrigramSimilarity('ism',soz)
                                                ).filter(oxshashlik__get=0.5)
        x = AktyorSerializer(aktyorlar, many=True)
        return Response(x.data)
#
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
#
# class BittaAktyorApiView(APIView):
#     def get(self, request, pk):
#         aktyorlar = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyorlar)
#         return Response(serializer.data)
#
# class OchirishAktyorApiView(APIView):
#     def delete(self, request, pk):
#         aktyor = Aktyor.objects.filter(id=pk).delete()
#         serializer = AktyorSerializer(aktyor)
#         return Response(serializer.data)

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
            return Response(serializers.data)
        return Response(serializers.errors)

class BittaIzohApiView(APIView):
    def get(self, request, pk):
        izohlar = Izoh.objects.get(id=pk)
        x = IzohSerializer(izohlar)
        return Response(x.data)

class KinoApiView(APIView):
    def get(self, request):
        soz = request.query_params.get('qidiruv')
        if soz:
            kino = Kino.objects.filter(nom__contains=soz)|Kino.objects.filter(janr=soz)
        else:
            kino = Kino.objects.all()

        x = KinoSerializer(kino, many=True)
        return Response(x.data, status=status.HTTP_200_OK)
    def post(self, request):
        malumot = request.data
        serializer = KinoSaqlashSerializer(data=malumot)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#
# class KinoDetailApiView(APIView):
#     def put(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         malumot = request.data
#         serializers = KinoSaqlashSerializer(kino, data=malumot)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class BittaKinoApiView(APIView):
#     def get(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializers = KinoSerializer(kino)
#         return Response(serializers.data, status=status.HTTP_410_GONE)
# class KinoDeleteApiView(APIView):
#     def delete(self, request, pk):
#         Kino.objects.filter(id=pk).delete()
#         return Response({"xabar":"Kino malumoti ochirildi"}, status=status.HTTP_202_ACCEPTED)

class AktyorModelViewSet(ModelViewSet):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism','davlat']
    ordering_fields = ['id','ism','tugulgan_yil','davlat']

class KinoModelViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nom','janr']
    ordering_fields = ['davomiylik','reyting']

    @action(detail=True, methods=['GET', 'POST'])
    def aktyorlar(self, rerquest, pk):
        if rerquest.method == 'POST':
            aktyor = rerquest.data
            kino = self.get_object()
            serializer = AktyorSerializer(data=aktyor)
            if serializer.is_valid():
                a = Aktyor.objects.create(
                    ism=serializer.validated_data.get('ism'),
                    davlat=serializer.validated_data.get('davlat'),
                    tugulgan_yil=serializer.validated_data.get('tugulgan_yil'),
                    jins=serializer.validated_data.get('jins'),
                )
                kino.aktyorlar.add()
                kino.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        kino = self.get_object()
        actors = kino.aktyorlar.all()
        serializer = AktyorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IzohModelViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Izoh.objects.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IzohDeleteViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            Izoh.objects.filter(user=request.user).delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        malumot = request.data
        user = authenticate(username = malumot.get("username"),
                            password = malumot.get("password"))
        if user is None:
            return Response({"success": "False", "xabar": "User topilmadi"})
        login(request, user)
        return Response({"success": "True", "xabar": "User login qilindi"})

class Logout(APIView):
    def get(self, request):
        logout(request)
        return Response({"success": "True", "xabar": "User logout qilindi"})



# Create your views here.
