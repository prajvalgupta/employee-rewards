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
				