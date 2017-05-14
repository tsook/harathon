from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Relation, Member
from .forms import moneyForm, memberForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers

def home_page(request):
	name=request.user.username
	groupid = Member.objects.get(username=name).group_id
	Alllist = Relation.objects.filter(group_id=groupid)
	Getlist = Alllist.filter(receiver=name)
	Paylist = Alllist.filter(giver=name)
	return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist, 'balance' : calculateBalance(Getlist, Paylist), 'name': name})

def new_Money(request):
	form = moneyForm()
	name=request.user.username
	if request.method == "POST":
		form = moneyForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.time = timezone.now()
			data.group_id = Member.objects.get(username=name).group_id
			data.save()
			return redirect('home_page')
		else:
			form = moneyForm()
	return render(request, 'finance/new_Money.html', {'form': form, 'name': name})

def delete(request):
	if request.GET:
		Relation.objects.all().filter(pk=request.GET['id']).delete()
		return HttpResponse('/completed/')

def get_list(request):
	if request.GET:
		name = request.user.username
		groupid = Member.objects.get(username=name).group_id
		json_data = serializers.serialize('json', Relation.objects.filter(group_id=groupid));
		return HttpResponse(json_data, content_type="application/json")

def calculateBalance(getlist, paylist):
	total = 0
	for entry in getlist:
		total += entry.money
	for entry in paylist:
		total -= entry.money
	return total

def signup(request):
    memForm = memberForm()
    if request.method == 'POST':
        memForm = memberForm(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid() and memForm.is_valid():
            data = memForm.save(commit=False)
            data.save()
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def simplify(request):
	name = request.user.username
	groupid = Member.objects.get(username=name).group_id
	Alllist = Relation.objects.filter(group_id=groupid)
	simplifyGraph(getNetBalanceList(Alllist), groupid)
	return redirect('home_page')

def getNetBalanceList(data):
	result = {}
	for entry in data:
		if entry.giver in result:
			result[entry.giver] -= entry.money
		else:
			result[entry.giver] = -1*entry.money
		if entry.receiver in result:
			result[entry.receiver] += entry.money
		else:
			result[entry.receiver] = entry.money

	toDelete = []
	for key in result.keys():
		if result[key] == 0:
			toDelete.append(key)

	for key in toDelete:
		del result[key]

	return result

def simplifyGraph(data, groupid):
	Relation.objects.filter(group_id=groupid).delete()
	while data:
		key_max = max(data.keys(), key=(lambda k: data[k]))
		key_min = min(data.keys(), key=(lambda k: data[k]))
		if data[key_max] > abs(data[key_min]):
			data[key_max] = data[key_max] + data[key_min]
			Relation.objects.create(giver=key_min, receiver=key_max, money=abs(data[key_min]), text="Combined", time=timezone.now(), group_id=groupid)
			del data[key_min]
		elif abs(data[key_min]) > data[key_max]:
			data[key_min] = data[key_max] + data[key_min]
			Relation.objects.create(giver=key_min, receiver=key_max, money=data[key_max], text="Combined", time=timezone.now(), group_id=groupid)
			del data[key_max]
		else:
			Relation.objects.create(giver=key_min, receiver=key_max, money=data[key_max], text="Combined", time=timezone.now(), group_id=groupid)
			del data[key_max]
			del data[key_min]