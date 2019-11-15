from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
from django.utils import timezone

# Create your models here.

# # Create your models here.
# class user_profile(models.Model):
# 	# user_name = models.CharField(max_length=50) #max_length = required
# 	# email = models.CharField(max_length=60) 
# 	# first_name = models.CharField(max_length=50)
# 	# last_name = models.CharField(max_length=50)
# 	user1 = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')	
# 	contact_number = models.CharField(max_length=20)
# 	zip_code = models.CharField(max_length=8)
# 	# password1 = models.CharField(max_length=20)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		user_profile.objects.create(user1=instance)
# 	instance.profile.save()



# employee model
# class employee(models.Model):
# 	eid = models.IntegerField(primary_key = True)
# 	ename = models.CharField(max_length=20) 
# 	password = models.CharField(max_length=20)
# 	admin = models.BooleanField(default = False)


# employee recieved point 
class RecievedPoints(models.Model):
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	timestamp = models.DateTimeField()
	PAmount = models.IntegerField()


# balanced point 
class BalancedPoints(models.Model):
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	PAmount = models.IntegerField()


# point transaction 
class PointTrans(models.Model):
	PTransId = models.IntegerField(primary_key = True)
	PTransDate = models.DateField() 
	pointAmount = models.IntegerField()
	received_eId = models.IntegerField()
	given_eId = models.ForeignKey(User, null=True, on_delete=models.PROTECT)


# employee redeemed giftcards 
class GiftCards(models.Model):
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	GAmount = models.IntegerField()


# giftcard transaction 
class GiftTrans(models.Model):
	GTransId = models.IntegerField(primary_key = True)
	GTransDate = models.DateField() 
	giftcardAmount = models.IntegerField()
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)