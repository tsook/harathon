from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Relation
from .forms import loginForm
from .forms import moneyForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from operator import attrgetter

def home_page(request):
	name=request.user.username
	Alllist = Relation.objects.all()
	simplifyGraph(getNetBalanceList(Alllist))
	Allist = Relation.objects.all()
	Getlist = Relation.objects.filter(receiver=name)
	Paylist = Relation.objects.filter(giver=name)
	return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist, 'balance' : calculateBalance(Getlist, Paylist), 'name': name})

def new_Money(request):
	form = moneyForm()
	name=request.user.username
	if request.method == "POST":
		form = moneyForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.time = timezone.now()
			data.save()
			return redirect('home_page')
		else:
			form = moneyForm()
	return render(request, 'finance/new_Money.html', {'form': form, 'name': name})

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class Person:
	def __init__(self, name, balance, info):
		self.name = name
		self.balance = balance
		self.info = info

def getNetBalanceList(data):
	result = {}
	for entry in data:
		if entry.giver in result:
			result[entry.giver].balance -= entry.money
			result[entry.giver].info += str(entry)
		else:
			result[entry.giver] = Person(entry.giver, -1*entry.money, str(entry))
		if entry.receiver in result:
			result[entry.receiver].balance += entry.money
			result[entry.receiver].info += str(entry) 
		else:
			result[entry.receiver] = Person(entry.receiver, entry.money, str(entry))

	for key in result.keys():
		if result[key].balance == 0:
			del result[key]
	return result

def simplifyGraph(data):
	data = list(data.values())
	Relation.objects.all().delete()
	while data:
		obj_max = max(data, key=attrgetter('balance'))
		obj_min = min(data, key=attrgetter('balance'))
		if obj_max.balance > abs(obj_min.balance):
			obj_max.balance = obj_max.balance + obj_min.balance
			Relation.objects.create(giver=obj_min.name, receiver=obj_max.name, money=abs(obj_min.balance), text="Combined: " + obj_min.info + " and " + obj_max.info, time=timezone.now())
			data.remove(obj_min)
		elif abs(obj_min.balance) > obj_max.balance:
			obj_min.balance = obj_max.balance + obj_min.balance
			Relation.objects.create(giver=obj_min.name, receiver=obj_max.name, money=obj_max.balance, text="Combined: " + obj_min.info + " and " + obj_max.info, time=timezone.now())
			data.remove(obj_max)
		else:
			Relation.objects.create(giver=obj_min.name, receiver=obj_max.name, money=obj_max.balance, text="Combined: " + obj_min.info + " and " + obj_max.info, time=timezone.now())
			data.remove(obj_max)
			data.remove(obj_min)