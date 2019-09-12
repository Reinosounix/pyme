from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from administrator import views
urlpatterns = [
    path('admin_main/', views.admin_main, name='admin_main'), 
    path('main_users/', views.main_users, name='main_users'),     
    path('new_users/', views.new_users, name='new_users'),     
    path('list_users/<group_id>/', views.list_users, name='list_users'),     
    path('list_users/<group_id>/<page>/', views.list_users, name='list_users'),     

    path('block_users/<user_id>/<group_id>/<page>/', views.block_users, name='block_users'),
    path('activate_users/<user_id>/<group_id>/<page>/', views.activate_users, name='activate_users'),
]  