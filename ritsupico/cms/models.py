from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
	userdata = models.CharField('username', mac_length = 255, default = 'NAME')
	whatdata = models.CharField('Datatype', max_length = 255, default = 'DATA')
