from django.db import models
from django.contrib.auth.models import User

class Aktyor(models.Model):
    tanlov = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    ]

    ism = models.CharField(max_length=50)
    davlat = models.CharField(max_length=50)
    tugulgan_yil = models.DateField()
    jins = models.CharField(max_length=10, choices=tanlov)
    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=100)
    janr = models.CharField(max_length=50)
    yil = models.DateField()
    davomiylik = models.DurationField()
    aktyorlar = models.ManyToManyField(Aktyor, related_name='aktyor')
    reyting = models.FloatField()
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    baho = models.PositiveSmallIntegerField()
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)


# Create your models here.
