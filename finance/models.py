from django.db import models
from django.utils import timezone

# Create your models here.

class Relation(models.Model):
    giver = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    money = models.IntegerField()
    text = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    