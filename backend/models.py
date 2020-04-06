from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class ExtendUser(models.Model):
    MALE = 'ML'
    FEMALE = 'FM'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    profile_pic = models.ImageField(verbose_name='Profile Picture', blank=True, null=True, upload_to='backend_uploads')
    gender = models.CharField(max_length=2, choices=GENDER, default=MALE, blank=False, null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.extenduser.save()




