from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import *
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
admin.site.register(MonthlyPoints)
admin.site.register(TotalPoints)
admin.site.register(PointTrans)
admin.site.register(GiftCards)
# admin.site.register(GiftTrans)

class PointsAdmin(admin.ModelAdmin):
    fields= ('PTransDate','pointAmount','received_eId','message','given_eId')
    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        if not hasattr(instance,'given_eId'):
            instance.given_eId = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change): 

        def set_user(instance):
            if not instance.given_eId:
                instance.given_eId = request.user
            instance.save()

        if formset.model == PointTrans:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
