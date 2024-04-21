from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings


def createProfile(sender,instance,created,**kwargs):
    print('inside signal')
    if created:
        user=instance
        print('user is created')
        subject='Welcome to GreenAura'
        message='We are glad you are here!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

post_save.connect(createProfile,sender=CustomUser)

