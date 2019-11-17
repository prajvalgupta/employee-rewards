import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')

import django
# Import settings
django.setup()

from random import randint, choice
from emp_reward.models import PointTrans, MonthlyPoints, TotalPoints, GiftCards
from faker import Faker
from django.contrib.auth.models import User
from dateutil import tz
import datetime

obj = Faker()



def points(N=10):
	num = 1

	for i in range(N):
		PTransDate = obj.date_time_between(start_date="-60d", end_date="now")
		pointAmount = obj.random_int(min=0, max=300)
		received_eId = User.objects.get(id=obj.random_element(elements=(1,2,3,4,5,6,7)))
		message = obj.paragraph(nb_sentences=2, variable_nb_sentences=True)
		given_eId = User.objects.get(id=obj.random_element(elements=(1,2,3,4,5,6,7)))

		# datee = datetime.datetime.strptime(PTransDate, "%Y-%m-%d")

		print(PTransDate.month)

		instance = MonthlyPoints.objects.get(eid = given_eId)

		if instance.balanceLeft>=pointAmount and received_eId!=given_eId:
			pointsTransc = PointTrans.objects.get_or_create(PTransDate =PTransDate, pointAmount = pointAmount, received_eId = received_eId, message = message, given_eId= given_eId  )
			
			if PTransDate.month==11:
				print("Yes")
				instance.balanceLeft-=pointAmount
				instance.save()
			try:
				total_instance = TotalPoints.objects.get(eid = received_eId)
				total_instance.PAmount+= pointAmount
			except:
				total_instance = TotalPoints()
				total_instance.eid = received_eId
				total_instance.PAmount = pointAmount
			total_instance.save()
			num+=1
		else:
			pass


def gifts(N=10):
	num = 1

	for i in range(N):
		PTransDate = obj.date_time_between(start_date="-60d", end_date="now")
		pointAmount = obj.random_int(min=0, max=50)
		received_eId = User.objects.get(id=obj.random_element(elements=(1,2,3,4,5,6,7)))

		total_instance = TotalPoints.objects.get(eid = received_eId)

		if total_instance.PAmount >= 10*pointAmount:
			giftcards = GiftCards.objects.create(timestamp =PTransDate, GAmount = pointAmount, eid = received_eId)
			total_instance.PAmount-= 10*pointAmount
			num+=1
		else:
			pass

if __name__ == '__main__':
	print("Filling data")
	points(50)
	gifts(20)
	print("Filling done")