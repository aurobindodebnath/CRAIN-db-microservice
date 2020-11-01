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
class appsecObservation(models.Model):
    CHOICES = (
		('High','High'),
		('Medium','Medium'),
		('Low','Low'),
		)
    observation = models.CharField(max_length=200)
    abbr = models.CharField(max_length=8)
    criticality = models.CharField(max_length=10,choices=CHOICES,default='High')
    detOb = models.TextField()
    risk= models.TextField()
    recommendation = models.TextField()
    comments = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.observation

class vaptObservation(models.Model):
  CHOICES = (
	('High','High'),
	('Medium','Medium'),
	('Low','Low'),
	)
  observation = models.CharField(max_length=200)
  abbr = models.CharField(max_length=8)
  criticality = models.CharField(max_length=10,choices=CHOICES,default='High')
  detOb = models.TextField()
  risk= models.TextField()
  recommendation = models.TextField()
  def __str__(self):
    return str(self.id) + ' - '+self.observation

class vaptPlugin(models.Model):
  pluginID = models.CharField(max_length=20)
  vapt_observation = models.ForeignKey(vaptObservation, on_delete=models.CASCADE)

  def __str__(self):
    return self.pluginID + ' - ' + self.vapt_observation.observation


class scrObservation(models.Model):
    CHOICES = (
		('High','High'),
		('Medium','Medium'),
		('Low','Low'),
		)
    LANGUAGE = (
      ('Java','Java'),
      ('Python','Python'),
    )
    observation = models.CharField(max_length=200)
    abbr = models.CharField(max_length=8)
    criticality = models.CharField(max_length=10,choices=CHOICES,default='High')
    language = models.CharField(max_length=10,choices=LANGUAGE)
    detOb = models.TextField()
    risk= models.TextField()
    recommendation = models.TextField()
    comments = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.observation
