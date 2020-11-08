from django.db import models
from django.conf import settings


# Create your models here.
class ServerAsset(models.Model):
    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )
    """服务器"""
    id = models.BigAutoField(primary_key=True, help_text="主键id")                                     #主键
    sn = models.CharField(max_length=128, unique=True, verbose_name="序列号", help_text="序列号")         # 不可重复
    name = models.CharField(max_length=64, unique=True, verbose_name="服务器名称", help_text="服务器名称")   # 不可重复
    os_name = models.CharField(max_length=128, verbose_name="操作系统名称", null=True, help_text="操作系统名称")
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,  models.PROTECT,
                                related_name='creator_id', null=True, verbose_name='记录者',)
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    updator = models.ForeignKey(settings.AUTH_USER_MODEL,  models.PROTECT,
                                related_name='updator_id', null=True, verbose_name='更新者',)
    flag_delted = models.BooleanField(null=True, default=False, verbose_name="删除标记")

    def __str__(self):
        return f'{self.name}({self.sn})'

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        # ordering = ('update_time', )
        # db_table = 'cmdb_server_asset'