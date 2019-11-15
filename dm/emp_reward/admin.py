from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
# class UserProfileInLine(admin.StackedInline):
#     model = user_profile
#     can_delete = False
#     verbose_name_plural = 'profile'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (UserProfileInLine, )

# Re-register UserAdmin
# admin.site.register(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(employee)
admin.site.register(RecievedPoints)
admin.site.register(BalancedPoints)
admin.site.register(PointTrans)
admin.site.register(GiftCards)
admin.site.register(GiftTrans)