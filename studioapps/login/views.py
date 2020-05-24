# -*- coding: utf-8 -*-
"""
登录相关业务逻辑
"""
from datetime import datetime

from django.views import View
from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from common.response import BaseAPIView
from studioapps.account.accounts import Account
from studioapps.login.serializers import LoginTokenSerializer
from studioapps.login.common.mixins.exempt import LoginExemptMixin


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


class APILoginView(BaseAPIView):
    """
    token登录方式
    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = LoginTokenSerializer(data=request.data)
        try:
            serializer.is_valid()
        except Exception as e:
            raise NotFound(e)

        user = serializer.object.get('user') or request.user
        token = serializer.object.get('token')
        refresh = serializer.object.get('refresh')
        return Response({'user': user.username, 'token': token, 'refresh': refresh})
