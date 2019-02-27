
from django.urls import path, include
from . import views

app_name = 'legalTech'

urlpatterns = [
    # path('', views.signIn, name='signIn'),
    # path('post', views.postsign, name='post'),
    path('', views.welcome, name='welcome'),
    path('addsponsor1', views.addsponsor1, name='addsponsor1'),
    path('addsponsor2', views.addsponsor2, name='addsponsor2'),
    path('addsponsor3', views.addsponsor3, name='addsponsor3'),




    
    path('addspeaker', views.addspeaker, name='addspeaker'),
    path('addexhibitor', views.addexhibitor, name='addexhibitor'),
    path('addschedule', views.addschedule, name='addschedule'),
    path('addattendee', views.addattendee, name='addattendee'),
    path('addmap', views.addmap, name='addmap'),
    path('addwifi', views.addwifi, name='addwifi'),
    path('addsocial', views.addsocial, name='addsocial'),
    path('addabout', views.addabout, name='addabout'),

    path('sponsors', views.sponsors, name='sponsors'),
    path('speaker', views.speaker, name='speaker'),
    path('exhibitor', views.exhibitor, name='exhibitor'),
    path('schedule', views.schedule, name='schedule'),
    path('attendee', views.attendee, name='attendee'),
    path('map', views.map, name='map'),
    path('wifi', views.wifi, name='wifi'),
    path('social', views.social, name='social'),
    path('about', views.about, name='about'),
    path('geticon/<slug:foo>', views.geticon, name='geticon'),
  
]
