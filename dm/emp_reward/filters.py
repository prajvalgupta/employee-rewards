from django.contrib.auth.models import User
import django_filters
from django_filters import widgets
from .models import *
from django import forms

class UserFilter(django_filters.FilterSet):
	# PTransDate = django_filters.DateTimeFromToRangeFilter(widget=widgets.RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

	PTransDate = django_filters.DateFilter(
        lookup_expr='icontains',
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'type': 'text'
            }
        )
    )
	class Meta:
		model = PointTrans
		fields = ['PTransDate', 'received_eId', ]



		