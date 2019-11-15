from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import *
from .models import *
from .tasks import *
from background_task import background
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.


def home(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')


def signup(request):
	# print(request.user)
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			auth_login(request,user)
			return redirect('home')
	else:
		form = UserForm()
	context = {
	'form': form
	}
	return render(request, 'signup.html', context)