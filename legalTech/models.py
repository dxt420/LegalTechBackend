from django.db import models

# # Create your models here.
class Sponsor(models.Model):
    icon = models.ImageField(upload_to='media/Sponsors/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)



class Exhibitor(models.Model):
    icon = models.ImageField(upload_to='media/Exhibitors/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)



class Speaker(models.Model):
    icon = models.ImageField(upload_to='media/Speaker/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)


class Attendee(models.Model):
    icon = models.ImageField(upload_to='media/Attendees/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)
    


