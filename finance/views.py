from django.shortcuts import render
from django.utils import timezone
from .models import user_data
from .forms import loginForm
from django.shortcuts import redirect

# Create your views here

def login_page(request):
	form = loginForm()
	if request.method == 'POST':
		form = loginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			return render(request, 'finance/home_page.html', {'name': data["name"]})
		else:
			form = loginForm()

	return render(request, 'finance/login_page.html', {'form': form})