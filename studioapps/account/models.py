from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from studioapps.account import constants


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, verbose_name=_("用户"), on_delete=models.CASCADE)
    real_name = models.CharField(max_length=20, verbose_name=_("姓名"))
    contact = models.CharField(max_length=18, verbose_name=_("联系方式"))
    email = models.CharField(max_length=20, verbose_name=_("邮箱地址"))
    permissionType = models.IntegerField(verbose_name='角色', choices=constants.PERMISSION_TYPE_CHOICES)

    def __str__(self):
        return '角色:{} - 姓名:{}'.format(constants.PERMISSION_TYPE_DICT[self.permissionType], self.real_name)

    class Meta:
        db_table = "ts_profile"
        verbose_name = "成员信息"
        verbose_name_plural = verbose_name
