from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .forms import *
from .models import *
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
from django.db.models.functions import TruncMonth, ExtractMonth
from django.db.models import Count, Sum, F, Q
from operator import attrgetter
from itertools import chain
from .tasks import add_points
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
			user_sess = PointTrans.objects.order_by('-PTransId')[0]
			# print(user_sess)
			user_sess.given_eId_id = request.user.id
			user_sess.save()
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
			messages.info(request, 'Points are transferred successfully')
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
			event.save()
			total_instance = TotalPoints.objects.get(eid = request.user)
			if total_instance.PAmount >= 10*event.cleaned_data.get('GAmount'):
				total_instance.PAmount-= 10*event.cleaned_data.get('GAmount')
				total_instance.save()
				event.save()
				user_sess = GiftCards.objects.order_by('-GTransId')[0]
				# print(user_sess)
				user_sess.eid = request.user
				user_sess.save()
				messages.info(request, 'GiftCard redeemed successfully')
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


def ResetPointsView(request):
	if request.user.is_authenticated:
		eids = User.objects.values_list('id',flat=True)
		print(eids)
		for eid in eids:
			instance = MonthlyPoints()
			user = User.objects.get(id=eid)
			print(user)
			instance.eid = user
			instance.PAmountReceived = 1000
			instance.balanceLeft = 1000
			instance.timestamp = timezone.now()
			instance.save()
			for row in MonthlyPoints.objects.all():
				if MonthlyPoints.objects.filter(eid=user).count() > 1:
					row.delete()

		return HttpResponse("Points are reset")
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
		summary = {}
		col_sum = {}
		result_list=[]

		mu_points = PointTrans.objects.annotate(month=ExtractMonth('PTransDate')).values('received_eId','given_eId','month').annotate(c=Sum('pointAmount')).order_by('-month')
		
		if request.user.is_superuser:
			users = User.objects.all()
			for user in users:
				summary[user.username] = PointTrans.objects.filter(given_eId_id=user.id).annotate(month=ExtractMonth('PTransDate')).values('received_eId','month').annotate(c=Sum('pointAmount')).order_by('-month')
		
		else:
			user = User.objects.get(id = request.user.id)
			summary[user.username] = PointTrans.objects.filter(Q(given_eId_id=user.id) | Q(received_eId_id = user.id)).annotate(month=TruncMonth('PTransDate')).values('received_eId', 'given_eId','month').annotate(c=Sum('pointAmount')).order_by('-month')


		total_given = PointTrans.objects.annotate(month=ExtractMonth('PTransDate'), eid= F('given_eId')).values('eid','month').annotate(points_given=Sum('pointAmount')).order_by('-month')
		total_received = PointTrans.objects.annotate(month=ExtractMonth('PTransDate'), eid= F('received_eId')).values('eid','month').annotate(points_Received=Sum('pointAmount')).order_by('-month')

		z = {**total_given[0], **total_received[0]}
		# print(z) 
		max_len = max(len(total_given),len(total_received))

		# for i in total_given:
		# 	total_given_list.append(i)

		# for i in total_received:
		# 	total_received_list.append(i)

		# print(total_given_list)
		# print(total_received_list)
		# result_list = sorted(
		# 	chain(total_given_list, total_received_list),
		# 	key=lambda points: points['eid'])

		bal_points = MonthlyPoints.objects.filter(balanceLeft__lte = 999).annotate(month=ExtractMonth('timestamp')).values('month','eid','balanceLeft').order_by('-month','-balanceLeft')
		# print(bal_points)

		for i in range(max_len):
			z = {**total_given[i], **total_received[i]}
			result_list.append(z)
		
		result = sorted(result_list, key = lambda i: i['points_Received'], reverse = True)	


		redeemed_points = GiftCards.objects.annotate(month=ExtractMonth('timestamp'), points = F('GAmount')*10).values('month','eid','GAmount','points').order_by('-month')
		
		# print(result)

		context = {
		'points': mu_points,
		'summary':summary,
		'monthly_det':result,
		'bal_points': bal_points,
		'redeemed_points':redeemed_points
		}
		return render(request, "points-info.html", context)
	else:
		# raise ValidationError("You are not authorized to add a venue (Admin only activity)") 
		messages.info(request, 'You are not logged in. Please login first to create an event')
		return redirect('login')



