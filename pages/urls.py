from django.urls import re_path
from . import views


urlpatterns = [
	re_path(r'^curriculum$', views.CurriculumView.as_view(), name='curriculum'),
	re_path(r'^gallery$', views.GalleryView.as_view(), name='gallery'),
	re_path(r'^sampleDay$', views.SampleDayView.as_view(), name='sampleDay'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^contact$', views.contact, name='contact'),
    re_path(r'^about$', views.AboutView.as_view(), name='about'),
    re_path(r'^inquiry$', views.InquiryView.as_view(), name='inquiry'),
    re_path(r'^faq$', views.FAQView.as_view(), name='faq'),
    re_path(r'^index$', views.IndexView.as_view(), name='index'),
    re_path(r'^$', views.WelcomePageView.as_view(), name='welcome'),
]