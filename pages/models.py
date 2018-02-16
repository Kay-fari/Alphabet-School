# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model):
    stu_name = models.CharField('Student Name', max_length=40)
    date_of_birth = models.DateField('Date of Birth')
    stu_address = models.CharField('Student Address', max_length=50, blank=False)
    city = models.CharField(max_length=30)
    # Parent or Guadian
    par_name = models.CharField('Parent Name', max_length=40)
    par_address = models.CharField('Parent Address', max_length=60, blank=False)
    home_telephone = models.CharField(max_length=40, blank=False)
    place_employment = models.CharField('Place of Employment', max_length=50, blank=True)
    work_telephone = models.CharField(max_length=40, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    # Parent or Guadian 2
    par_name2 = models.CharField('Parent Name', max_length=40)
    par_address2 = models.CharField('Parent Address 2', max_length=60, blank=False)
    home_telephone2 = models.CharField('Home Telephone', max_length=40, blank=False)
    place_employment2 = models.CharField('Place of Employment', max_length=50, blank=True)
    work_telephone2 = models.CharField('Work Telephone', max_length=40, blank=True)
    occupation2 = models.CharField('Occupation', max_length=50, blank=True)
    email2 = models.EmailField('Email Address')

    def __str__(self):
        return str(self.stu_name)
