from django.conf.urls import *
from django.urls import path

from . import view,account

urlpatterns = [
    url(r'^$',view.login),
    path('vertify/',view.veritify),
    path('search/',view.search),
    path('insert/',view.insert),
    path('regist/',view.regist),
    path('code/',view.code),

]