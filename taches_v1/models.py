from django.db import models
from django.utils import timezone
from datetime import timedelta, datetime

# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Tache(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    statut = models.BooleanField(default=False)
    date_creation = models.DateTimeField(default=timezone.now, null=True, blank=True)
    date_echeance = models.DateTimeField(default=timezone.now, null=True, blank=True)


    def __str__(self):
        return self.titre

class FilterTache(models.Model):
    est_terminer = models.BooleanField(default=False)
    date_debut = models.DateField(default=datetime.now() - timedelta(days=30), null=True, blank=True)
    date_fin = models.DateField(default=timezone.now, null=True, blank=True)