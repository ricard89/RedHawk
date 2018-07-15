# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#from django.contrib.auth.models import User
#from accounts.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Tag(models.Model):

    TAG_TYPE = (
        ("BOOL", "BOOL"),
        ("INTEGER", "INTEGER"),
        ("REAL", "REAL"),
    )

    WIDGETS = (
        ("LIGHT", "LIGHT"),
        ("BUTTON", "BUTTON"),
        ("SWITCH", "SWITCH"),
        ("PARAMETER", "PARAMETER"),
        ("DISPLAY", "DISPLAY"),
    )

    id = models.AutoField(primary_key=True)
    num_ID = models.SmallIntegerField()
    name_ID = models.CharField(max_length=20)
    value = models.CharField(max_length=20, default="", blank=True, null=True)
    unit = models.CharField(max_length=20, default="", blank=True, null=True)
    type = models.CharField(max_length=20, choices=TAG_TYPE)
    widget = models.CharField(max_length=20, choices=WIDGETS)
    device = models.CharField(max_length=20, default="", blank=True, null=True)
    arguments = models.CharField(max_length=200, default="", blank=True, null=True)
    owner = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('num_ID', 'owner'), ('name_ID', 'owner'))

    def __str__(self):
        return_string = self.name_ID
        return return_string


class Notification(models.Model):

    OPERATORS = (
        ("==", "=="),
        ("<=", "<="),
        (">=", ">="),
        ("<", "<"),
        (">", ">"),
        ("=!", "=!"),
    )

    id = models.AutoField(primary_key=True)
    num_ID = models.SmallIntegerField()
    first_operand = models.ForeignKey(Tag, on_delete=models.CASCADE)
    operator = models.CharField(max_length=20, choices=OPERATORS)
    second_operand = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    sended = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
