from django.contrib import admin
from .models import farmer,farm,cli

# Register your models here.
class showadmin(admin.ModelAdmin):
     model='farmer'
     list_display=['name','image','designation']
     list_editable =('image','designation',)
     list_filter = ('designation',)
admin.site.register(farmer,showadmin)
admin.site.register(farm)
admin.site.register(cli)
