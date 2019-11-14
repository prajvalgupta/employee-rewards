from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import DateInput

class UserForm(UserCreationForm):
	# user_name = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
	email = forms.EmailField(max_length=254, help_text='Please provide a valid email address.')
	# password1 = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
