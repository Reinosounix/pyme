from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404,redirect

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField(upload_to=custom_upload_to,null=True, blank=True)
    name = models.CharField(max_length = 240,null=True, blank=True)
    last_name = models.CharField(max_length = 240,null=True, blank=True)
    specialty = models.CharField(max_length = 240,null=True, blank=True)
    payment = models.CharField(max_length = 240,null=True, blank=True)
    sex = models.CharField(max_length = 240,null=True, blank=True)    
    birthdate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length = 240,null=True, blank=True)
    commune = models.CharField(max_length = 240,null=True, blank=True)
    address = models.CharField(max_length = 240,null=True, blank=True)
    phone = models.CharField(max_length = 240,null=True, blank=True)
    mobile = models.CharField(max_length = 240,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)