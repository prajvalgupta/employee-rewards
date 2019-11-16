"""dm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emp_reward import views as main_views
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from emp_reward.tasks import add_points

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main_views.home, name='home'),
    url(r'^signup/$', main_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^points-transfer/$', main_views.pointTranscview, name='pointsTransfer'),
    url(r'^redeem/$', main_views.GiftCardRedeemView, name='giftcard-redeem'),
    # url(r'^search/$', main_views.search, name='search')
    url(r'^search/$', main_views.sortPoints, name='search'),
    url(r'^reset/$', main_views.ResetPointsView, name='reset')
]

add_points(repeat = 2592000)