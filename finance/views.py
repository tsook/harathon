from django.shortcuts import render
from django.utils import timezone
from .models import user_data

# Create your views here.
def home_page(request):
	UserData = user_data.objects.all()
	return render(request, 'finance/home_page.html', {'UserData' : UserData})

def login_page(request):
	return render(request, 'finance/login_page.html', {})