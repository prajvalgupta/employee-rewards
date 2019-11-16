from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib import messages
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
from .filters import UserFilter
from django.template.defaulttags import register
from django.http import HttpRequest
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
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


def pointTranscview(request):
	if request.user.is_authenticated:
		event = PointsTransferForm(request.POST or None)
		if event.is_valid():
			event.save()
			instance = MonthlyPoints.objects.get(eid = request.user)
			instance.balanceLeft-=event.cleaned_data.get('pointAmount')
			instance.save()
			print(event.cleaned_data.get('received_eId'))
			user_name = event.cleaned_data.get('received_eId')
			user_inst = User.objects.get(username = user_name)
			try:
				total_instance = TotalPoints.objects.get(eid = user_inst)
				total_instance.PAmount+= event.cleaned_data.get('pointAmount')
			except:
				total_instance = TotalPoints()
				total_instance.eid = user_inst
				total_instance.PAmount = event.cleaned_data.get('pointAmount')
			total_instance.save()
			event = PointsTransferForm()
		context = {
		'events': event
		}
		return render(request, "points-transfer.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to create an event')
		return redirect('login')

def GiftCardRedeemView(request):
	if request.user.is_authenticated:
		event = GiftCardRedeemForm(request.POST or None)
		if event.is_valid():
			event.eid = request.user
			total_instance = TotalPoints.objects.get(eid = request.user)
			if total_instance.PAmount >= 10*event.cleaned_data.get('GAmount'):
				total_instance.PAmount-= 10*event.cleaned_data.get('GAmount')
				total_instance.save()
				event.save()
			else:
				messages.info(request, 'You dont have enough amount to redeem a giftcard')
			event = GiftCardRedeemForm()
		context = {
		'events': event
		}
		return render(request, "giftcard-redeem.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to create an event')
		return redirect('login')

def search(request):
	user_list = PointTrans.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'user_list.html', {'filter': user_filter})


def sortPoints(request):
	if request.user.is_authenticated:
			
		points = PointTrans.objects.annotate(month=TruncMonth('PTransDate')).values('received_eId','month').annotate(c=Sum('pointAmount')).order_by('month')
		context = {
		'points': points
		}
		return render(request, "points-info.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to create an event')
		return redirect('login')



