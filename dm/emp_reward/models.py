from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
from django.utils import timezone
# from cms.utils.permissions import get_current_user 
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
class MonthlyPoints(models.Model):
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	timestamp = models.DateTimeField()
	PAmountReceived = models.IntegerField()
	balanceLeft = models.IntegerField()

# total point 
class TotalPoints(models.Model):
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	PAmount = models.IntegerField()


# point transaction 
class PointTrans(models.Model):
	PTransId = models.AutoField(primary_key = True)
	PTransDate = models.DateTimeField(null=True) 
	pointAmount = models.IntegerField()
	received_eId = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name= "points_received_by")
	message = models.CharField(max_length=240,null=True)
	given_eId = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name= "points_given_by")

	# def save(self, *args, **kwargs):
	# 	user = get_current_user()
	# 	if user and not user.pk:
	# 		user = None
	# 	if not self.pk:
	# 		self.given_eId = user
	# 	super(PointTrans, self).save(*args, **kwargs)
# employee redeemed giftcards 
class GiftCards(models.Model):
	GTransId = models.AutoField(primary_key = True)
	eid = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
	timestamp = models.DateTimeField(null = True)
	GAmount = models.IntegerField(null=True)