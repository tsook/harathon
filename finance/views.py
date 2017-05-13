from django.shortcuts import render
from django.utils import timezone
from .models import Relation
from .forms import loginForm
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
	Alllist = Relation.objects.all()
	Getlist = Relation.objects.filter(receiver__lte="A")
	Paylist = Relation.objects.filter(giver__lte="A")

	return render(request, 'finance/home_page.html', {'UserData' : Alllist, 'Getlist' : Getlist, 'Paylist' : Paylist})

def login_page(request):
	form = loginForm()
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			return redirect('home_page', name=data.name)
		else:
			form = loginForm()

	return render(request, 'finance/login_page.html', {'form': form})
