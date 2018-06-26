# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from main_app.models import Tag, Notification

# Register your models here.
admin.site.register(Tag)
admin.site.register(Notification)
