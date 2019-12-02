# -*- coding: utf-8 -*-
import json
import logging
from collections import OrderedDict
from rest_framework import exceptions
from rest_framework.views import APIView, exception_handler
from common import error_code
from django.utils.translation import gettext as _

logger = logging.getLogger("api-request")


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    request = context['request']

    if response is not None:
        data = response.data
        response.data = {}
        if 'detail' in data and not isinstance(data['detail'], (list, dict)):

            if isinstance(data['detail'], str):
                data['detail'] = data['detail']

            if hasattr(error_code, data['detail']):
                response.data['return_code'] = getattr(error_code, data['detail'])
                response.data['return_msg'] = _(getattr(error_code.ZhError, data['detail']))
                logger.error("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                    "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                    "return": json.dumps(response.data), "data": data})
            elif isinstance(data['detail'], exceptions.ErrorDetail):
                code = str(data['detail'].code).upper()
                if hasattr(error_code, code):
                    response.data['return_code'] = getattr(error_code, code)
                    response.data['return_msg'] = _(getattr(error_code.ZhError, code))
                    logger.error("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                        "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                        "return": json.dumps(response.data), "data": data})
                else:
                    response.data['return_code'] = getattr(error_code, 'SYSTEM_ERROR')
                    response.data['return_msg'] = _(data['detail'])
                    logger.error("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                        "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                        "return": json.dumps(response.data), "data": data})
            else:
                response.data['return_code'] = getattr(error_code, 'SYSTEM_ERROR')
                response.data['return_msg'] = _(data['detail'])
                logger.error("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                    "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                    "return": json.dumps(response.data), "data": data})
        else:
            if isinstance(exc, exceptions.ValidationError):
                response.data['return_code'] = getattr(error_code, 'ERROR_CHECK_PARAM')
                # response.data['return_msgEn'] = getattr(error_code.EnglishError, 'ERROR_CHECK_PARAM')
                response.data['return_msg'] = _(getattr(error_code.ZhError, 'ERROR_CHECK_PARAM'))
                response.data['data'] = data
                try:
                    logger.error("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                        "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                        "return": json.dumps(response.data), "data": data})
                    pass
                except Exception as e:
                    pass
            else:
                response.data['return_code'] = getattr(error_code, 'UNDIFINED_ERROR')
                response.data['return_msg'] = _(getattr(error_code.ZhError, 'UNDIFINED_ERROR'))
                response.data['data'] = data
                try:
                    logger.critical("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
                        "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data),
                        "return": json.dumps(response.data), "data": data})
                except Exception as e:
                    pass

    else:
        logger.critical("route:%(route)s\trequest:%(request)s\treturn:%(return)s\tdata:%(data)s" % {
            "route": json.dumps(request.build_absolute_uri()), "request": json.dumps(request.data), "return": "None",
            "data": repr(exc)})

    return response


class Version2APIView(APIView):
    def get_exception_handler(self):
        return custom_exception_handler


class BaseAPIView(Version2APIView):
    def finalize_response(self, request, response, *args, **kwargs):
        response = super(BaseResponse, self).finalize_response(request, response, *args, **kwargs)

        if hasattr(response, 'render') and callable(response.render):
            response.render()

        if 200 <= response.status_code < 300:
            if response.get('Content-Type', "").lower() == 'application/json':
                response.content = json.dumps({"return_code": 0, "return_msg": _('成功'),
                                               "data": json.loads(response.content, object_pairs_hook=OrderedDict)})
            else:
                if str(response.content).lower() != "success":
                    response.content = json.dumps(
                        {"return_code": 0, "return_msg": _('成功'), "data": _(response.content)})
                else:
                    response.content = json.dumps({"return_code": 0, "return_msg": _('成功')})
                response['Content-Type'] = 'application/json'
        return response

    def encode_error(self, error_no):

        if hasattr(error_code, error_no):
            return {
                'return_code': getattr(error_code, error_no),
                'return_msg': _(getattr(error_code.ZhError, error_no))
            }
        else:
            return {
                'return_code': getattr(error_code, 'SYSTEM_ERROR'),
                'return_msg': _(error_no)
            }
