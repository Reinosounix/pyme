from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from core import views
urlpatterns = [
    path('', views.home, name='home'), 
    path('check_group_main', views.check_group_main, name='check_group_main'),
]  