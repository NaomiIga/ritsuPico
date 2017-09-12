from django.contrib import admin
from cms.models import Data
admin.site.register(Data)

# Register your models here.
class DataAdmin(admin.ModelAdmin):
	list_display = ('userdata', 'datavalue',)
	list_display_links = ('userdata',)
admin.site.register(Data, DataAdmin)
