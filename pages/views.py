# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import ContactForm

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'pages/index.html'

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class InquiryView(TemplateView):
    template_name = 'pages/inquiry.html'

class FAQView(TemplateView):
    template_name = 'pages/faq.html'

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




