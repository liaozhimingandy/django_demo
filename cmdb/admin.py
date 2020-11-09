from django.contrib import admin
from . import models


# Register your models here.
class ServerAssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'sn', 'name', 'os_type', 'manage_ip', 'create_time',
                    'update_time', 'memo', 'flag_delted']
    list_filter = ['name', 'manage_ip', 'status', 'flag_delted']
    list_editable = ['sn', 'name', 'os_type', 'manage_ip',
                     'memo', 'flag_delted']
    search_fields = ('sn',)


# admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.ServerAsset, ServerAssetAdmin)