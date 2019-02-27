from django.shortcuts import render
from google.cloud import storage
# Create your views here.

from . models import *
from django.http import  HttpResponseRedirect
from django.urls import reverse

from pyrebase import pyrebase 
import os

import time
from datetime import datetime
from django.conf import settings
import re
import numpy as np
import json
import ast


config = {
    'apiKey': "AIzaSyDFNW8MN6rPrdwJnxV1S_RLPX2dgg4gVNg",
    'authDomain': "legaltech-7887b.firebaseapp.com",
    'databaseURL': "https://legaltech-7887b.firebaseio.com",
    'projectId': "legaltech-7887b",
    'storageBucket': "legaltech-7887b.appspot.com",
    'messagingSenderId': "470663134509"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


email="admin@alt.com"
passw = "legaltech2019"

user = auth.sign_in_with_email_and_password(email,passw)

# def signIn(request):
#     return render(request, "legalTech\signIn.html")

def welcome(request):
    # goldsponsors = db.child("sponsors").child("gold").get()
    # log(goldsponsors.val())
    return render(request, "legalTech\welcome.html",{"e":email})

def sponsors(request):  
    goldsponsors = db.child("sponsors").child("gold").get()
    silversponsors = db.child("sponsors").child("silver").get()
    platinumsponsors = db.child("sponsors").child("platinum").get()

    
    return render(request, "legalTech\sponsors.html",{"goldsponsors":goldsponsors,"silversponsors":silversponsors,"platinumsponsors":platinumsponsors})
# def postsign(request):
#     email=request.POST.get('email')
#     passw = request.POST.get("pass")
#     try:
#         user = auth.sign_in_with_email_and_password(email,passw)
#     except:
#         message = "invalid cerediantials"
#         return render(request,"legalTech\signIn.html",{"msg":message})
#     print(user)
#     return render(request, "legalTech\welcome.html",{"e":email})


def exhibitor(request):
    exhibitors = db.child("exhibitors").get()
    return render(request, "legalTech\exhibitor.html",{"exhibitors":exhibitors})

def speaker(request):
    speakers = db.child("speakers").get()
    return render(request, "legalTech\speaker.html",{"speakers":speakers})

def attendee(request):
    attendees = db.child("users").get()
    return render(request, "legalTech\attendee.html",{"attendees":attendees})

def schedule(request):
    schedule = db.child("schedule").get()
    speakers = db.child("speakers").get()
    return render(request, "legalTech\schedule.html",{"schedule":schedule,"speakers":speakers})

def about(request):
    about = db.child("about").get()
    return render(request, "legalTech\about.html",{"about":about})

def social(request):
    social = db.child("social").get()
    return render(request, "legalTech\social.html",{"social":social})

def map(request):
    mapp = db.child("map").get()
    return render(request, "legalTech\map.html",{"map":mapp})

def wifi(request):
    wifi = db.child("wifi").get()
    return render(request, "legalTech\wifi.html",{"wifi":wifi})




def geticon(request,id):
    icon = Sponsor.objects.get(firebase_id_token=id)
    return icon.url


def addsponsor1(request):
    
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    thename = request.FILES['pic']
    new_sponsor_pic = Sponsor(icon=request.FILES['pic'])      
    new_sponsor_pic.save()
    print(new_sponsor_pic.icon.url)
    s = new_sponsor_pic.icon.url + " "
    s = re.sub('/.*?/', '', s)
    print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("sponsors/"+s).put(filer + new_sponsor_pic.icon.url, user['idToken'])
    url = storage.child("sponsors/"+s).get_url(user['idToken'])
    data = {
        "name": request.POST.get('name'),
        "info": request.POST.get('info'),
        "description": request.POST.get('description'),
        "website": request.POST.get('website'),
        "email": request.POST.get('email'),
        "phone": request.POST.get('phone') ,
        "imageurl": url
    }

    results = db.child("sponsors").child("gold").push(data, user['idToken'])
    
    return HttpResponseRedirect(reverse('legalTech:sponsors'))
    


def addsponsor2(request):
    
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    thename = request.FILES['pic']
    new_sponsor_pic = Sponsor(icon=request.FILES['pic'])      
    new_sponsor_pic.save()
    print(new_sponsor_pic.icon.url)
    s = new_sponsor_pic.icon.url + " "
    s = re.sub('/.*?/', '', s)
    print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("sponsors/"+s).put(filer + new_sponsor_pic.icon.url, user['idToken'])
    url = storage.child("sponsors/"+s).get_url(user['idToken'])
    data = {
        "name": request.POST.get('name'),
        "info": request.POST.get('info'),
        "description": request.POST.get('description'),
        "website": request.POST.get('website'),
        "email": request.POST.get('email'),
        "phone": request.POST.get('phone') ,
        "imageurl": url
    }

    results = db.child("sponsors").child("platinum").push(data, user['idToken'])
    
    return HttpResponseRedirect(reverse('legalTech:sponsors'))


def addsponsor3(request):
    
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    thename = request.FILES['pic']
    new_sponsor_pic = Sponsor(icon=request.FILES['pic'])      
    new_sponsor_pic.save()
    print(new_sponsor_pic.icon.url)
    s = new_sponsor_pic.icon.url + " "
    s = re.sub('/.*?/', '', s)
    print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("sponsors/"+s).put(filer + new_sponsor_pic.icon.url, user['idToken'])
    url = storage.child("sponsors/"+s).get_url(user['idToken'])
    data = {
        "name": request.POST.get('name'),
        "info": request.POST.get('info'),
        "description": request.POST.get('description'),
        "website": request.POST.get('website'),
        "email": request.POST.get('email'),
        "phone": request.POST.get('phone') ,
        "imageurl": url
    }

    results = db.child("sponsors").child("silver").push(data, user['idToken'])
    
    return HttpResponseRedirect(reverse('legalTech:sponsors'))


def addexhibitor(request):
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    thename = request.FILES['pic']
    new_sponsor_pic = Exhibitor(icon=request.FILES['pic'])      
    new_sponsor_pic.save()
    print(new_sponsor_pic.icon.url)
    s = new_sponsor_pic.icon.url + " "
    s = re.sub('/.*?/', '', s)
    print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("exhibitors/"+s).put(filer + new_sponsor_pic.icon.url, user['idToken'])
    url = storage.child("exhibitors/"+s).get_url(user['idToken'])
    data = {
        "name": request.POST.get('name'),
        "company": request.POST.get('company'),
        "info":request.POST.get('info'),
        "imageurl": url
    }


    results = db.child("exhibitors").push(data, user['idToken'])
    
    return HttpResponseRedirect(reverse('legalTech:exhibitor'))


def addspeaker(request):
    now = datetime.today().strftime("%Y%m%d%H%M%S")
    
    storage = firebase.storage()
    # as user
    thename = request.FILES['pic']
    new_sponsor_pic = Exhibitor(icon=request.FILES['pic'])      
    new_sponsor_pic.save()
    print(new_sponsor_pic.icon.url)
    s = new_sponsor_pic.icon.url + " "
    s = re.sub('/.*?/', '', s)
    print(s)
    filer = re.sub('media', '', settings.MEDIA_ROOT)
    storage.child("speakers/"+s).put(filer + new_sponsor_pic.icon.url, user['idToken'])
    url = storage.child("speakers/"+s).get_url(user['idToken'])
    data = {
        "name": request.POST.get('name'),
        "company": request.POST.get('company'),
        "info":request.POST.get('info'),
        "imageurl": url
    }


    results = db.child("speakers").push(data, user['idToken'])
    
    return HttpResponseRedirect(reverse('legalTech:speaker'))



def addattendee(request):
    return render(request,"legalTech\attendee.html",{"msg":message})

def addschedule(request):
    c = dict(request.POST.lists())
    # d = request.POST.getlist('checks')
    print(type(c["checks"]))
    arr = []
    for a in c["checks"]:
        arr.append(''.join(a))
        
    

    # print(arr)

    # k =  c["checks"].list()
    # print(k)
    # print(type(k))
    # print(c["checks"])
    # print(d)
    # print(ast.literal_eval(c["checks"]))
    # print(type(ast.literal_eval(c["checks"])))

    data = {
        "time": request.POST.get('time'),
        "title": request.POST.get('title'),
        "details": request.POST.get('details')
            

    }

    

    print(type(data))

    results = db.child("schedule").push(data, user['idToken'])
    
    for a in arr:
        print(a)
        ast.literal_eval(a)
        print(ast.literal_eval(a))
        print(type(ast.literal_eval(a)))
        db.child("schedule").child(results["name"]).child("speakers").push(ast.literal_eval(a), user['idToken'])
    # db.child("schedule").push(data, user['idToken'])
    
    print(results["name"])
    return HttpResponseRedirect(reverse('legalTech:schedule'))
    

def addabout(request):
    db.child("about").update({"meetingattire": request.POST.get('meetingattire')}, user['idToken'])  
    db.child("about").update({"transport": request.POST.get('transport')}, user['idToken'])  
    db.child("about").update({"venue": request.POST.get('venue')}, user['idToken'])  
    results = db.child("about").push(data, user['idToken'])
    return HttpResponseRedirect(reverse('legalTech:about'))

def addsocial(request):
    db.child("social").update({"facebook": request.POST.get('facebook')}, user['idToken'])  
    db.child("social").update({"twitter": request.POST.get('twitter')}, user['idToken'])  
    db.child("social").update({"linkedin": request.POST.get('linkedin')}, user['idToken'])  
    return HttpResponseRedirect(reverse('legalTech:social'))

def addmap(request):
    db.child("map").update({"directions": request.POST.get('directions')}, user['idToken'])
    return HttpResponseRedirect(reverse('legalTech:map'))

def addwifi(request):
    db.child("wifi").update({"username": request.POST.get('username')}, user['idToken'])
    db.child("wifi").update({"password": request.POST.get('password')}, user['idToken'])
    return HttpResponseRedirect(reverse('legalTech:wifi'))