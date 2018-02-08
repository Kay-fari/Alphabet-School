from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^about$', views.AboutView.as_view(), name='about'),
    re_path(r'^inquiry$', views.InquiryView.as_view(), name='inquiry'),
    re_path(r'^faq$', views.FAQView.as_view(), name='faq'),
    re_path(r'^$', views.IndexView.as_view(), name='index'),
]