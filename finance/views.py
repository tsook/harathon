from django.shortcuts import render
from django.utils import timezone
from .models import Relation
from .forms import loginForm
from .forms import moneyForm
from django.shortcuts import redirect
from django.http import HttpResponse

def login_page(request):
	form = loginForm()
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			name = data["name"]
			Alllist = Relation.objects.all()
			Getlist = Relation.objects.filter(receiver=name)
			Paylist = Relation.objects.filter(giver=name)

			return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist, 'balance' : calculateBalance(Getlist, Paylist), 'name': name})
		else:
			form = loginForm()

	return render(request, 'finance/login_page.html', {'form': form})

def new_Money(request):
	form = moneyForm()
	if request.method == "POST":
		form = moneyForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.time = timezone.now()
			data.save()
			return redirect('home_page')
		else:
			form = moneyForm()
	return render(request, 'finance/new_Money.html', {'form': form})


def delete(request):
	if request.GET:
		Relation.objects.all().filter(pk=request.GET['id']).delete()
		return HttpResponse('/completed/')


def canvas_test(request):
	return render(request, 'finance/canvas_test.html', {})

def calculateBalance(getlist, paylist):
	total = 0
	for entry in getlist:
		total += entry.money
	for entry in paylist:
		total -= entry.money
	return total
