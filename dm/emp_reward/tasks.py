from .models import *
from background_task import background
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User

@background(schedule = 60)
def add_points():
	eids = User.objects.values_list('id',flat=True)
	print(eids)
	for eid in eids:
		balance = BalancedPoints()
		instance = RecievedPoints()
		user = User.objects.get(id=eid)
		print(user)
		instance.eid = user
		instance.PAmount = 1000
		instance.timestamp = timezone.now()
		balance.eid = user
		balance.PAmount = 1000
		balance.save()
		instance.save()
		for row in RecievedPoints.objects.all():
			if RecievedPoints.objects.filter(eid=user).count() > 1:
				row.delete()
		for row in BalancedPoints.objects.all():
			if BalancedPoints.objects.filter(eid=user).count() > 1:
				row.delete()