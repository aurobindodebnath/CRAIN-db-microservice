from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class allObservations(models.Model):
    CHOICES = (
		('High','High'),
		('Medium','Medium'),
		('Low','Low'),
		)
    TYPE_CHOICE = (
		('Application Security','Application Security'),
		('Network Architecture Review','Network Architecture Review'),
		('Vulnerability Assessment', 'Vulnerability Assessment'),
		('Mobile Application Security','Mobile Application Security'),
		)
    ptype = models.CharField(max_length=40,choices=TYPE_CHOICE,default='Application Security')
    observation = models.CharField(max_length=200)
    abbr = models.CharField(max_length=8)
    criticality = models.CharField(max_length=10,choices=CHOICES,default='High')
    detOb = models.TextField()
    risk= models.TextField()
    recommendation = models.TextField()
    def __str__(self):
        return self.observation
