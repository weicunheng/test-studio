# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy as _

# 系统错误
UNDEFINED_ERROR = 91000
SYSTEM_ERROR = 91001
ERROR_CHECK_PARAM = 90001
ERROR_DB_OP = 90002
ERROR_CHECK_SIGN = 90010
ERROR_TIME_OUT = 90011
ERROR_FORBIDDEN = 90024

# 用户相关
NOT_AUTHENTICATED = 90003
AUTHENTICATION_FAILED = 90004
TOKEN_NOT_VALID = 90005
ERROR_USERNAME_PASSWORD_CANNOT_BE_EMPTY = 90006

# 测试项目
ERROR_NOT_EXIST_PROJECT = 90100


class ZhError(object):
    UNDEFINED_ERROR = _('未定义的错误')
    SYSTEM_ERROR = _('系统错误')
    ERROR_CHECK_PARAM = _('验证参数失败')
    ERROR_DB_OP = _('服务器开了会小差')
    ERROR_TIME_OUT = _('请求时间过长')
    ERROR_CHECK_SIGN = _('验证签名失败')
    ERROR_FORBIDDEN = _('对不起您没有操作的权限')

    NOT_AUTHENTICATED = _('用户未登录')
    AUTHENTICATION_FAILED = _('用户认证失败')
    TOKEN_NOT_VALID = _('用户认证失败')
    ERROR_USERNAME_PASSWORD_CANNOT_BE_EMPTY = _("用户名密码不能为空")

    ERROR_NOT_EXIST_PROJECT = _('项目不存在')
    ERROR_PROJECT_IS_EXIST = _('项目已经存在')
