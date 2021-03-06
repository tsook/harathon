from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Member(models.Model):
	group_id = models.CharField(max_length = 5)
	username = models.CharField(max_length=20)

	def __str__(self):
		return "[Group: " + self.group_id + ". Username: " + self.username + "]"

class Relation(models.Model):
    giver = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    money = models.IntegerField()
    text = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    group_id = models.CharField(max_length=5)

    def __str__(self):
    	return "[" + self.giver + " owes " + self.receiver + " W" + str(self.money) + " because " + self.text + "] "
