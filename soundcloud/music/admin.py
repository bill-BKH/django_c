from django.contrib import admin
from .models import Music,Genres,Singer
# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title','year','singer']
    list_filter = ['year']
    list_editable = ['year','singer']
    
    
admin.site.register(Music, MusicAdmin)
admin.site.register(Genres)
admin.site.register(Singer)


