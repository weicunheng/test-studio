# -*- coding: utf-8 -*-
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
    (AppStatusEnum.LOCAL, "提测中"),
    (AppStatusEnum.DEV, "开发中"),
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
