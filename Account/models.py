from django.db import models
from django.contrib.auth.models import User
from uuid import *

class Yazar(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	forUser_uiid = models.CharField(max_length=255,default='Hey')
	
	def save(self,*args,**kwargs):
		self.forUser_uuid=uuid4()
		super().save(*args,**kwargs)

