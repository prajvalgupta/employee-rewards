from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import DateInput
from django.utils import timezone
from crum import get_current_user 
import django_filters
from django_filters import widgets

class UserForm(UserCreationForm):
	# user_name = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
	email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.')
	# password1 = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class PointsTransferForm(forms.ModelForm):
	pointAmount = forms.IntegerField(label="How many points?")
	received_eId = forms.ModelChoiceField(label="Who do you want to give the points to?",queryset=User.objects.all(), empty_label="(Nothing)")
	message = forms.CharField(widget=forms.Textarea,label="Do you want to add some thank you note?",max_length=240)

	def __init__(self, *args, **kwargs):
		super(PointsTransferForm, self).__init__(*args, **kwargs)
		queryset = self.fields['received_eId'].queryset
		choices = [(poll.pk, poll.username) for poll in queryset]
		self.fields['received_eId'].choices = choices

	def save(self, commit=True):
		obj = super(PointsTransferForm, self).save(commit=False)
		user = get_current_user()
		if obj.given_eId is None:
			obj.PTransDate = timezone.now()
		if commit:
			obj.save()
		return obj
	class Meta:
		model = PointTrans
		fields = ('pointAmount','received_eId','message')



class GiftCardRedeemForm(forms.ModelForm):
	
	GAmount = forms.IntegerField(label="How many points you want to redeem?")

	def save(self, commit=True):
		obj = super(GiftCardRedeemForm, self).save(commit=False)
		user = get_current_user()
		if obj.eid is None:
			obj.timestamp = timezone.now()
		if commit:
			obj.save()
		return obj

	class Meta:
		model = GiftCards
		fields = ('GAmount',)


# class SortPointsForm(forms.Form):

# 	PTransDate = forms.DateField(
#         widget=forms.DateInput(
#             attrs={
#                 'id': 'datepicker',
#                 'type': 'text'
#             }
#         )
#     )

# 	class Meta:	
# 		fields = ('PTransDate','received_eId')




	