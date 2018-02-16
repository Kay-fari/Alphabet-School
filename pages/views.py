# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.urls import reverse_lazy

from pages.models import Register
from .forms import ContactForm, RegistrationForm

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


# Create your views here.


class IndexView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class InquiryView(TemplateView):
    template_name = 'pages/inquiry.html'

class FAQView(TemplateView):
    template_name = 'pages/faq.html'

class SampleDayView(TemplateView):
    template_name = 'pages/sampleDay.html'

class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'

class WelcomePageView(TemplateView):
    template_name = 'pages/welcomePage.html'

class CurriculumView(TemplateView):
    template_name = 'pages/curriculum.html'        
        

# Contact Form view.
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteownder@example.com'],
                connection=con,
            )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form':form,
    }
    return render(request, 'pages/contact.html', context)

# Registration Form View
def register(request):
    submitted = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()

            return HttpResponseRedirect('/register?submitted=True')

    else:
        form = RegistrationForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form':form,
        'submitted':submitted,
    }

    return render(request, 'pages/register.html', context)













