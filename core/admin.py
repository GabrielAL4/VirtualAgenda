from django.contrib import admin
from core.models import Evento

# Register your models here.
class DisplayHour(admin.ModelAdmin):
    list_display = ('title', 'eventData', 'creationData')
    list_filter = ('title', 'user','eventData')



admin.site.register(Evento, DisplayHour)