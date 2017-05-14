from django.contrib import admin
from django.contrib.auth.models import User
from .models import Relation, Member

# Register your models here.
admin.site.register(Relation)
admin.site.register(Member)