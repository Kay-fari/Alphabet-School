# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Register
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('stu_name', )

admin.site.register(Register, RegisterAdmin)
