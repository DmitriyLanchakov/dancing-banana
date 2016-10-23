from django.contrib import admin

from api.models import Event
class EventAdmin(admin.ModelAdmin):
    list_display = ('coc_location_id', 'client_id', 'created')
    search_fields = ('coc_location_id', 'client_id')
admin.site.register(Event, EventAdmin)

from api.models import Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'created')
    search_fields = ('last_name',)
admin.site.register(Client, ClientAdmin)

from api.models import Coc
class CocAdmin(admin.ModelAdmin):
    list_display = ('name', 'coc_type', 'created')
    search_fields = ('name', 'coc_type')
admin.site.register(Coc, CocAdmin)