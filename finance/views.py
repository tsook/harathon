from django.shortcuts import render
from django.utils import timezone
from .models import user_data
from .forms import loginForm
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
	UserData = user_data.objects.all()
	return render(request, 'finance/home_page.html', {'UserData' : UserData})

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