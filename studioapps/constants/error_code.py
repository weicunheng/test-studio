# -*- coding: utf-8 -*-
UNDIFINED_ERROR = 91000
SYSTEM_ERROR = 91001
ERROR_CHECK_PARAM = 90001
ERROR_DB_OP = 90002
ERROR_EXIST_ORDER = 90003
ERROR_NOT_EXIST_ORDER = 90004
ERROR_EXIST_CHANNEL = 90005
ERROR_NOT_EXIST_CHANNEL = 90006
ERROR_EXIST_THIRD_ORDER = 90007
ERROR_NOT_EXIST_THIRD_ORDER = 90008
ERROR_REQUEST_TIME_OUT = 90009
ERROR_CHECK_SIGN = 90010
ERROR_TIME_OUT = 90011
ERROR_INVILID_TIMESTAMP = 90012
ERROR_ORDER_STATUS = 90013
ERROR_CHECK_ORDER_MONEY = 90014
ERROR_CHECK_CODE_STATUS = 90015
ERROR_CHECK_LOGIN = 90016
ERROR_MOBILE_EXIST = 90017
ERROR_MOBILE_NOT_EXIST = 90018
ERROR_SEND_SMS = 90019
ERROR_CHECK_MOBILE_TOKEN = 90020
ERROR_ALREADY_BIND_MOBILE = 90021
ERROR_NOT_BIND_MOBILE = 90022
ERROR_FIND_MODULE = 90023
ERROR_FORBIT = 90024
ERROR_SEND_SMS_LIMIT = 90025
ERROR_SAME_WITH_PREVIOUS = 90026
ERROR_CHECK_CODE = 90027
ERROR_CODE_EXPIRED = 90028
ERROR_CODE_USED = 90029
ERROR_CODE_OCCUPY = 90030
ERROR_ACCOUNT_EXIST = 90031
ERROR_ACCOUNT_NOT_EXIST = 90032
ERROR_CARD_NOT_EXIST = 90033
ERROR_OPERATE_SELF = 90034
ERROR_USERNAME_OR_PASSWORD = 90035
ERROR_IN_PROCESSING = 90036
ERROR_DEAL = 90037
ERROR_INVILID_ORDER_STATUS = 90038
ERROR_REFUND = 90039
ERROR_BOX_NOT_EXIST = 90040


class EnglishError(object):
    UNDIFINED_ERROR = 'undifined error'
    SYSTEM_ERROR = 'system error'
    ERROR_CHECK_PARAM = 'check params fail'
    ERROR_DB_OP = 'an error occured when operate database'
    ERROR_EXIST_ORDER = 'cashier order is exist'
    ERROR_NOT_EXIST_ORDER = 'cashier order is not exist'
    ERROR_EXIST_CHANNEL = 'channel is exist'
    ERROR_NOT_EXIST_CHANNEL = 'channel is not exist'
    ERROR_EXIST_THIRD_ORDER = 'third order number is exist'
    ERROR_NOT_EXIST_THIRD_ORDER = 'third order number is not exist'
    ERROR_TIME_OUT = 'request time out'
    ERROR_CHECK_SIGN = 'check sign error'
    ERROR_INVILID_TIMESTAMP = 'invilid timestamp'
    ERROR_ORDER_STATUS = 'the status of order is fail'
    ERROR_CHECK_ORDER_MONEY = 'an error occured when checking money from cashier'
    ERROR_CHECK_CODE_STATUS = 'the status of code is invilid'
    ERROR_CHECK_LOGIN = 'user is unauthorized'
    ERROR_MOBILE_EXIST = 'mobile is exist'
    ERROR_MOBILE_NOT_EXIST = 'mobile does not exist'
    ERROR_SEND_SMS = 'send sms error'
    ERROR_CHECK_MOBILE_TOKEN = 'token uploaded is not equal to the store one'
    ERROR_ALREADY_BIND_MOBILE = 'consumer has already bind mobile'
    ERROR_NOT_BIND_MOBILE = 'consumer does not bind mobile'
    ERROR_FIND_MODULE = 'the module you want to find is gone with the wind'
    ERROR_FORBIT = 'forbit!'
    ERROR_SEND_SMS_LIMIT = 'the times of sending sms is over'
    ERROR_SAME_WITH_PREVIOUS = 'the mobile you want to change is same with the previous one'
    ERROR_CHECK_CODE = 'code is invilid'
    ERROR_CODE_EXPIRED = 'code has expired'
    ERROR_CODE_USED = 'code is used'
    ERROR_CODE_OCCUPY = 'this code belongs to someone not you'
    ERROR_ACCOUNT_EXIST = 'account is exist'
    ERROR_ACCOUNT_NOT_EXIST = 'account is not exist'
    ERROR_CARD_NOT_EXIST = 'card is not exist'
    ERROR_OPERATE_SELF = 'can\'t operate myself'
    ERROR_USERNAME_OR_PASSWORD = 'error username or password'
    ERROR_IN_PROCESSING = 'still in process'
    ERROR_DEAL = 'already deal'
    ERROR_INVILID_ORDER_STATUS = 'invilid order status'
    ERROR_REFUND = 'refund fail'
    ERROR_BOX_NOT_EXIST = 'box is not exist'


class ZhError(object):
    UNDIFINED_ERROR = '未定义的错误'
    SYSTEM_ERROR = '系统错误'
    ERROR_CHECK_PARAM = '验证参数失败'
    ERROR_DB_OP = '服务器开了会小差'
    ERROR_EXIST_ORDER = '订单已存在'
    ERROR_NOT_EXIST_ORDER = '订单不存在'
    ERROR_EXIST_CHANNEL = '商户渠道已存在'
    ERROR_NOT_EXIST_CHANNEL = '商户渠道不存在'
    ERROR_EXIST_THIRD_ORDER = '商户订单号已存在，请勿重复下单'
    ERROR_NOT_EXIST_THIRD_ORDER = '商户订单号不存在'
    ERROR_TIME_OUT = '请求时间过长'
    ERROR_CHECK_SIGN = '验证签名失败'
    ERROR_INVILID_TIMESTAMP = '无效的时间戳'
    ERROR_ORDER_STATUS = '订单状态不正确'
    ERROR_CHECK_ORDER_MONEY = "验证订单金额失败"
    ERROR_CHECK_CODE_STATUS = "优惠码重复使用异常"
    ERROR_CHECK_LOGIN = "用户未登录"
    ERROR_MOBILE_EXIST = "手机号码已存在"
    ERROR_MOBILE_NOT_EXIST = "手机号码不存在"
    ERROR_SEND_SMS = "发送短信失败"
    ERROR_CHECK_MOBILE_TOKEN = '手机验证码验证失败'
    ERROR_ALREADY_BIND_MOBILE = '您已经绑定过手机了'
    ERROR_NOT_BIND_MOBILE = '您还未绑定过手机了'
    ERROR_FIND_MODULE = '操作对象不存在'
    ERROR_FORBIT = '对不起您没有操作的权限'
    ERROR_SEND_SMS_LIMIT = '超过短信发送限制'
    ERROR_SAME_WITH_PREVIOUS = "不能和原号码一样"
    ERROR_CHECK_CODE = '优惠码无效'
    ERROR_CODE_EXPIRED = '优惠码已过期'
    ERROR_CODE_USED = '优惠码已被使用'
    ERROR_CODE_OCCUPY = '优惠码已被领取过了'
    ERROR_ACCOUNT_EXIST = '账号已存在'
    ERROR_ACCOUNT_NOT_EXIST = '账号不存在'
    ERROR_CARD_NOT_EXIST = '卡券不存在'
    ERROR_OPERATE_SELF = '此操作不能对本人使用'
    ERROR_USERNAME_OR_PASSWORD = '用户名或者密码错误'
    ERROR_IN_PROCESSING = '正在处理中'
    ERROR_DEAL = '已经处理过了'
    ERROR_INVILID_ORDER_STATUS = '订单状态错误'
    ERROR_REFUND = '提现失败'
    ERROR_BOX_NOT_EXIST = '盒子不存在'