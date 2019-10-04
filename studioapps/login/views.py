# -*- coding: utf-8 -*-
"""
登录相关业务逻辑
"""
from datetime import datetime
from django.views import View
from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from studioapps.account.accounts import Account
from studioapps.login.serializers import LoginTokenSerializer
from studioapps.login.common.mixins.exempt import LoginExemptMixin


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class LoginView(LoginExemptMixin, View):
    """
    登录
    """
    def get(self, request):
        return self.post(request)

    def post(self, request):
        if settings.LOGIN_TYPE != "custom_login":
            account = Account()
            return account.login(request)

        custom_login_view = import_string(settings.CUSTOM_LOGIN_VIEW)
        return custom_login_view.post(request)


class APILoginView(APIView):
    """
    token登录方式
    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = LoginTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
