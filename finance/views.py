from django.shortcuts import render
from django.utils import timezone
from .models import Relation

# Create your views here.
def home_page(request):
	Alllist = Relation.objects.all()
	Getlist = Relation.objects.filter(receiver__lte="A")
	Paylist = Relation.objects.filter(giver__lte="A")

	return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist})