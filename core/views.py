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

def home(request):
    template_name = "core/home.html"
    return render(request,template_name)

@login_required
def check_group_main(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id ==0:
        pass
    if profiles.group_id ==1:
        return redirect('home')
    if profiles.group_id ==2:
        pass
    if profiles.group_id ==3:
        pass
    if profiles.group_id ==4:
        pass