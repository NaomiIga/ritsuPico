from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

# test
"""
class Data(models.Model):
	userdata = models.CharField('username', max_length = 255, default = 'NAME')
	whatdata = models.CharField('Datatype', max_length = 255, default = 'DATA')
"""
# User data
class User(models.Model):
	user_id = models.IntegerField('user_id', default = 0)
	username = models.CharField('username', max_length = 255, default = 'NAME')
	points = models.IntegerField('points', default = 0)
	starttime = models.DateTimeField('starttime', null=True, blank=True)
	finishtime = models.DateTimeField('finishtime', null=True, blank=True)
	treasures = models.CharField('treasures',max_length = 255, default = 'treasures')
	treasure1 = models.DateTimeField('treasure1', null=True, blank=True)
	treasure2 = models.DateTimeField('treasure2', null=True, blank=True)
	treasure3 = models.DateTimeField('treasure3', null=True, blank=True)
	treasure4 = models.DateTimeField('treasure4', null=True, blank=True)
	treasure5 = models.DateTimeField('treasure5', null=True, blank=True)
	treasure6 = models.DateTimeField('treasure6', null=True, blank=True)
	key_time = models.FloatField('key_time', default = 0)
	key = models.CharField('key', max_length = 1023, default = 'key')
	shopname = models.CharField('shopname', max_length = 255, default = 'SHOP')
	relationship = models.CharField('relationship', max_length = 255, default = 'relationship')

# User no hint siyou jyoukyou
class UsedHint(models.Model):
	username = models.CharField('username', max_length = 255, default = 'NAME')
	hint1_1 = models.DateTimeField('hint1-1', null=True, blank=True)
	hint1_2 = models.DateTimeField('hint1-2', null=True, blank=True)
	hint1_3 = models.DateTimeField('hint1-3', null=True, blank=True)
	hint2_1 = models.DateTimeField('hint2-1', null=True, blank=True)
	hint2_2 = models.DateTimeField('hint2-2', null=True, blank=True)
	hint2_3 = models.DateTimeField('hint2-3', null=True, blank=True)
	hint3_1 = models.DateTimeField('hint3-1', null=True, blank=True)
	hint3_2 = models.DateTimeField('hint3-2', null=True, blank=True)
	hint3_3 = models.DateTimeField('hint3-3', null=True, blank=True)
	hint4_1 = models.DateTimeField('hint4-1', null=True, blank=True)
	hint4_2 = models.DateTimeField('hint4-2', null=True, blank=True)
	hint4_3 = models.DateTimeField('hint4-3', null=True, blank=True)
	hint5_1 = models.DateTimeField('hint5-1', null=True, blank=True)
	hint5_2 = models.DateTimeField('hint5-2', null=True, blank=True)
	hint5_3 = models.DateTimeField('hint5-3', null=True, blank=True)
	hint6_1 = models.DateTimeField('hint6-1', null=True, blank=True)
	hint6_2 = models.DateTimeField('hint6-2', null=True, blank=True)
	hint6_3 = models.DateTimeField('hint6-3', null=True, blank=True)
	hint7_1 = models.DateTimeField('hint7-1', null=True, blank=True)
	hint7_2 = models.DateTimeField('hint7-2', null=True, blank=True)
	hint7_3 = models.DateTimeField('hint7-3', null=True, blank=True)
	hint8_1 = models.DateTimeField('hint8-1', null=True, blank=True)
	hint8_2 = models.DateTimeField('hint8-2', null=True, blank=True)
	hint8_3 = models.DateTimeField('hint8-3', null=True, blank=True)
	hint9_1 = models.DateTimeField('hint9-1', null=True, blank=True)
	hint9_2 = models.DateTimeField('hint9-2', null=True, blank=True)
	hint9_3 = models.DateTimeField('hint9-3', null=True, blank=True)
	hint10_1 = models.DateTimeField('hint10-1', null=True, blank=True)
	hint10_2 = models.DateTimeField('hint10-2', null=True, blank=True)
	hint10_3 = models.DateTimeField('hint10-3', null=True, blank=True)



# Not Change: treasure and beaconNo wo himoduke
class Treasure_Beacon(models.Model):
	treasure = models.IntegerField('treasure', default = 0)
	beacon_id = models.IntegerField('beacon', default = 0)
	major = models.IntegerField('major', default = 0)
	minor = models.IntegerField('minor', default = 0)

# Not Change: ikitaiSHOP to beaconNo wo himoduke
class Shop_Beacon(models.Model):
	shopname = models.CharField('shopname', max_length = 255, default = 'SHOPNAME')
	shop_id = models.IntegerField('shop_id', default = 0)
	major = models.IntegerField('major', default = 0)
	minor = models.IntegerField('minor', default = 0)
	floor = models.IntegerField('floor', default = 0)

# Not Change: beacon list
class Beacon(models.Model):
	beacon_id = models.IntegerField('beacon', default = 0)
	uuid = models.IntegerField('uuid', default = 0)
	major = models.IntegerField('major', default = 0)
	minor = models.IntegerField('minor', default = 0)
	category = models.CharField('category', max_length = 255, default = 'CATEGORY')

# Not Change: Hint list
class Hint(models.Model):
	treasure_num = models.IntegerField('treasure_num', default = 0)
	hint_num = models.IntegerField('hint_num', default = 0)
	hint_sent = models.CharField('hint_sentence', max_length = 255, default = 'HINT')
