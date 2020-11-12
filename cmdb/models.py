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
    os_type = (
        ('W', 'Windows'),
        ('A', 'Apple'),
        ('L', 'Linux')
    )
    """服务器"""
    id = models.BigAutoField(primary_key=True, help_text="主键id")  # 主键
    sn = models.CharField(max_length=128, unique=True, verbose_name="序列号", help_text="序列号")  # 不可重复
    name = models.CharField(max_length=64, unique=True, verbose_name="服务器名称", help_text="服务器名称")  # 不可重复
    # os_name = models.CharField(max_length=128, verbose_name="操作系统名称", null=True, help_text="操作系统名称")
    os_type = models.CharField(choices=os_type, default='W', max_length=2, blank=True, null=True, verbose_name="操作系统名称")
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')
    manage_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='管理IP')
    memo = models.TextField(null=True, blank=True, verbose_name='备注', max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT,
                                related_name='creator_id', null=True, verbose_name='记录者', )
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    updator = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT,
                                related_name='updator_id', null=True, verbose_name='更新者', )
    flag_delted = models.BooleanField(null=True, default=False, verbose_name="删除标记")

    def __str__(self):
        return f'{self.name}({self.sn})'

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        ordering = ('update_time', )
        # db_table = 'cmdb_server_asset'


# 数据库清单模型
class DatabaseAsset(models.Model):
    """数据库选择类型"""
    db_type = {
        ("MSSQL", "SQL Server"),
        ("Oracle", "Oracle"),
        ("Linux", "Linux")
    }

    """数据库"""
    id = models.BigAutoField(primary_key=True, help_text="主键id")
    db_type = models.CharField(choices=db_type, blank=False, null=False, verbose_name="数据库类型", max_length=8)
    db_version = models.CharField(max_length=128, null=True, blank=True, verbose_name="数据库版本信息")
    username = models.CharField(max_length=32, verbose_name="登录用户名", help_text="登录用户名")
    password = models.CharField(max_length=32, verbose_name="登录密码", help_text="登录密码")
    manage_ip = models.ForeignKey(ServerAsset, on_delete=models.RESTRICT,
                                  related_name='server_id', null=True, verbose_name='所在服务器')
    port = models.IntegerField(verbose_name="数据库端口号", default="4433")
    memo = models.TextField(null=True, blank=True, verbose_name='备注', max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT,
                                related_name='db_creator_id',null=True, verbose_name='记录者')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    updator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT,
                                related_name='db_updator_id',null=True, verbose_name='更新者')
    flag_delted = models.BooleanField(null=True, default=False, verbose_name="删除标记")

    def __str__(self):
        return f'{self.db_type}({self.db_version})'

    class Meta:
        verbose_name = '数据库清单表'
        verbose_name_plural = "数据库清单表"
        ordering = ('update_time', )
        # db_table = 'cmdb_server_asset'