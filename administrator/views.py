import json
from datetime import datetime, timedelta, time
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Q
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail, EmailMultiAlternatives
from registration.models import Profile

def admin_main(request):
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intento ingresar a un área para la cual Su perfil de usuario no tiene permisos')      
        return redirect('check_group_main')
    template_name = "administrator/admin_main.html"
    return render(request,template_name)
@login_required
def main_users(request):
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intento ingresar a un área para la cual Su perfil de usuario no tiene permisos')      
        return redirect('check_group_main')
    template_name = 'administrator/main_users.html'
    return render(request,template_name)
@login_required
def new_users(request):
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intento ingresar a un área para la cual Su perfil de usuario no tiene permisos')      
        return redirect('check_group_main')
    groups = Group.objects.all().order_by('name').exclude(pk=0)
    if request.method == 'POST':
        grupo = request.POST.get('grupo')
        rut = request.POST.get('rut')
        first_name = request.POST.get('name')
        last_name_1 = request.POST.get('last_name1')
        last_name_2 = request.POST.get('last_name2')
        last_name = last_name_1+' '+last_name_2
        email = request.POST.get('email')
        rut_exist = User.objects.filter(username=rut).count()
        mail_exist = User.objects.filter(email=email).count()
        if rut_exist == 0:
            if mail_exist == 0:
                user = User.objects.create_user(
                    username= rut,
                    email=email,
                    password=rut,
                    first_name=first_name,
                    last_name=last_name,
                    )
                profile = Profile.objects.filter(user_id = user.id).update(group_id = grupo,name=first_name,last_name=last_name)
                messages.add_message(request, messages.INFO, 'Usuario creado con exito')                             
            else:
                messages.add_message(request, messages.INFO, 'El correo que esta tratando de ingresar, ya existe en nuestros registros')                             
        else:
            messages.add_message(request, messages.INFO, 'El rut que esta tratando de ingresar, ya existe en nuestros registros')                         
    template_name = 'administrator/new_users.html'
    return render(request,template_name,{'groups':groups})
@login_required
def list_users(request,group_id,page=None):
    profile = Profile.objects.get(user_id = request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intento ingresar a un área para la cual Su perfil de usuario no tiene permisos')      
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page')
    group = Group.objects.get(pk=group_id)
    users = User.objects.filter(profile__group_id=group_id).exclude(is_superuser='t').order_by('-is_active','first_name')
    paginator = Paginator(users, 10)  
    users_list = paginator.get_page(page)
    template_name = "administrator/list_users.html"
    return render(request,template_name, {'users_list':users_list,'paginator':paginator,'page':page,'group':group})
@login_required
def block_users(request,user_id,group_id,page=None):
    User.objects.filter(pk=user_id).update(is_active='f')
    messages.add_message(request, messages.INFO, 'Usuario bloqueado con éxito')                             
    return redirect('list_users',group_id,page)
@login_required
def activate_users(request,user_id,group_id,page=None):
    User.objects.filter(pk=user_id).update(is_active='t')
    messages.add_message(request, messages.INFO, 'Usuario activado con éxito')                             
    return redirect('list_users',group_id,page)
