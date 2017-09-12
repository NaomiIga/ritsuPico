from django.contrib import admin
from cms.models import *
#admin.site.register(Data)

# Register your models here.
class DataAdmin(admin.ModelAdmin):
	list_display = ('userdata', 'datavalue',)
	list_display_links = ('userdata',)
admin.site.register(Data, DataAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'username', 'starttime', 'finishtime', 'treasures', 'points', 'relationship',)
	list_display_links = ('username',)
	search_fields = ['user_id', 'username',]

class UsedHintAdmin(admin.ModelAdmin):
	list_display = ('username',)
	list_display_links = ('username',)

class BeaconAdmin(admin.ModelAdmin):
	list_display = ('beacon_id', 'uuid', 'major', 'minor', 'category',)
	list_display_links = ('beacon_id',)
'''
class Shop_BeaconAdmin(admin.ModelAdmin):
	list_display = ('shopname', 'shop_id', 'major', 'minor', 'floor')
	list_display_links = ('shopname', 'shop_id', 'major', 'minor',)
	search_fields = ['shopname', 'floor']
'''
class TreasureAdmin(admin.ModelAdmin):
	list_display = ('treasure', 'beacon_id',)
	list_display_links = ('treasure', 'beacon_id',)

class HintAdmin(admin.ModelAdmin):
	list_display = ('treasure_num', 'hint_num', 'hint_sent',)
	list_display_links = ('hint_num', 'hint_sent',)


admin.site.register(User, UserAdmin)
admin.site.register(UsedHint, UsedHintAdmin)
admin.site.register(Beacon, BeaconAdmin)
#admin.site.register(Shop_Beacon, Shop_BeaconAdmin)
admin.site.register(Treasure_Beacon, TreasureAdmin)
admin.site.register(Hint, HintAdmin)
admin.site.register(Data, DataAdmin)