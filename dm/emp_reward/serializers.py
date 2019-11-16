from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class PointsSerializer(serializers.ModelSerializer):
	class Meta:
		model = PointTrans
		fields = ('PTransDate','pointAmount','received_eId','message','given_eId')

