# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


class PermissionType(object):
    ADMIN = 0
    DEVELOPER = 1
    TESTER = 2


PERMISSION_TYPE_CHOICES = [
    (PermissionType.ADMIN, _('管理员')),
    (PermissionType.DEVELOPER, _('开发人员')),
    (PermissionType.TESTER, _('测试人员')),
]
PERMISSION_TYPE_DICT = dict(PERMISSION_TYPE_CHOICES)
