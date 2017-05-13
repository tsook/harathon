from django.shortcuts import render
from django.utils import timezone
from .models import Relation
from .forms import loginForm
from django.shortcuts import redirect

def login_page(request):
	form = loginForm()
	Alllist = Relation.objects.all()
	Getlist = Relation.objects.filter(receiver__lte="A")
	Paylist = Relation.objects.filter(giver__lte="A")
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist, 'name': data["name"]})
		else:
			form = loginForm()

	return render(request, 'finance/login_page.html', {'form': form})

def canvas_test(request):
	return render(request, 'finance/canvas_test.html', {})