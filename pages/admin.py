# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Register
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('stu_name', 'stu_address', 'city', 'par_name',
                    'par_address', 'home_telephone', 'work_telephone',
                    'occupation', 'email', )
    fieldsets = (
        (None, {
            'fields':('stu_name', 'stu_address', 'city'),
        }),
        ('Parent/Guardian Information 1', {
            'classes':('collapse',),
            'fields':('par_name', 'par_address', 'home_telephone',
                      'place_employment', 'work_telephone',
                      'occupation', 'email'),
        }),
        ('Parent/Guardian Information II', {
            'classes':('collapse'),
            'fields':('par_name2', 'par_address2', 'home_telephone2',
                      'place_employment2', 'work_telephone2',
                      'occupation2', 'email2'),
        }),
    )

admin.site.register(Register, RegisterAdmin)
