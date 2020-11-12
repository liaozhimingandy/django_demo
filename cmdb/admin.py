from django.contrib import admin
from . import models


# Register your models here.
class ServerAssetAdmin(admin.ModelAdmin):
    list_display = ['id', 'sn', 'name', 'os_type', 'manage_ip', 'create_time', "creator",
                    'update_time', 'memo', 'flag_delted']
    list_filter = ['name', 'manage_ip', 'status', 'flag_delted']
    list_editable = ['sn', 'name', 'os_type', 'manage_ip',
                     'flag_delted']
    search_fields = ('sn',)


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """
    该类用于显示 admin 内置的 django_admin_log 表。
    其中，content_type 是指用户修改的 Model 名
    """
    list_display = ['action_time', 'user', 'content_type', '__str__']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15
    readonly_fields = ['action_time', 'user', 'content_type',
                       'object_id', 'object_repr', 'action_flag', 'change_message']


@admin.register(models.DatabaseAsset)
class DatabaseAssetAdmin(admin.ModelAdmin):
    list_display = ["id", "db_type", "db_version", "username", "password", "manage_ip", "port", "memo",
                    "create_time", "creator"]
    list_display_links = ["id"]
    list_filter = ["db_type", "db_version", "username", "password", "manage_ip", ]
    list_per_page = 15
    search_fields = ["db_type", "db_version", "username", "manage_ip", "port", ]

# admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.ServerAsset, ServerAssetAdmin)



