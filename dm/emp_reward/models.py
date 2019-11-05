from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# employee model
class employee(models.Model):
	eid = models.IntegerField(primary_key = True)
	ename = models.CharField(max_length=20) 
	password = models.CharField(max_length=20)
	admin = models.BooleanFiel(default = False)


# employee recieved point 
class RecievedPoints(models.Model):
	eid = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)
	PAmount = models.IntegerField()


# balanced point 
class BalancedPoints(models.Model):
	eid = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)
	PAmount = models.IntegerField()


# point transaction 
class PointTrans(models.Model):
	PTransId = models.IntegerField(primary_key = True)
	PTransDate = models.DateField() 
	pointAmount = models.IntegerField()
	received_eId = models.IntegerField()
	given_eId = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)


# employee redeemed giftcards 
class GiftCards(models.Model):
	eid = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)
	GAmount = models.IntegerField()


# giftcard transaction 
class GiftTrans(models.Model):
	GTransId = models.IntegerField(primary_key = True)
	GTransDate = models.DateField() 
	giftcardAmount = models.IntegerField()
	eid = models.ForeignKey(employee, null=True, on_delete=models.PROTECT)