# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
"""
常量定义
"""


class AppStatusEnum(object):
    LOCAL = 0
    DEV = 1
    TESE = 2
    PROD = 3
    OFFLINE = 4


APP_STATUS_CHOICES = [
    (AppStatusEnum.DEV, "开发中"),
    (AppStatusEnum.LOCAL, "提测中"),
    (AppStatusEnum.TESE, "测试中"),
    (AppStatusEnum.PROD, "已上线"),
    (AppStatusEnum.OFFLINE, "已下线"),
]

APP_STATUS_CHOICES_DICT = dict(APP_STATUS_CHOICES)


class AppLanguage(object):
    PYTHON = 0
    JAVA = 1
    PHP = 2


APP_LANGUAGE_CHOICES = [
    (AppLanguage.PYTHON, "Python"),
    (AppLanguage.JAVA, "Java"),
    (AppLanguage.PHP, "PHP"),
]


class ProjectEnvironmentEnum(object):
    LOCAL = 1001
    DEV = 1002
    UAT = 1003
    PROD = 1004


PROJECT_ENVIRON_CHOICES = (
    (ProjectEnvironmentEnum.LOCAL, _("本地环境")),
    (ProjectEnvironmentEnum.DEV, _("测试环境")),
    (ProjectEnvironmentEnum.UAT, _("验收环境")),
    (ProjectEnvironmentEnum.PROD, _("生产环境")),
)

PROJECT_ENVIRON_CHOICES_DICT = dict(PROJECT_ENVIRON_CHOICES)
