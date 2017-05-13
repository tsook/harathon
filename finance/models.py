from django.db import models
from django.utils import timezone
import json

# Create your models here.
class user_data(models.Model):
        user = models.ForeignKey('auth.User')
        pay_list = models.TextField()
        get_list = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def __str__(self):
            return ("user: " + self.user + 
            		"pay_list: " + self.pay_list +
            		"get_list: " + self.get_list)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def set_pay_list(self, new_data):
        	self.pay_list = json.dumps(new_data)
        	return self.pay_list

        def get_pay_list(self):
        	return json.loads(self.pay_list)

        def append_pay_data(self, new_data):
        	list = self.get_pay_list()
        	list.append(new_data)
        	self.set_pay_list(self, list)
        	return self.pay_list

        def set_get_list(self, new_data):
        	self.get_list = json.dumps(new_data)
        	return self.get_list

        def get_get_list(self, new_data):
        	return json.loads(self.pay_list)

        def append_get_data(self, new_data):
        	list = self.get_get_list()
        	list.append(new_data)
        	self.set_get_list(self, list)
        	return self.get_list




