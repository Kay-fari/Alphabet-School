from django.urls import path
from pages import views


urlpatterns = [
    path('curriculum/', views.CurriculumView.as_view(), name='curriculum'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('sampleDay/', views.SampleDayView.as_view(), name='sampleDay'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('', views.WelcomePageView.as_view(), name='welcome'),
]