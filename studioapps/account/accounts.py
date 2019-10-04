# -*- coding: utf-8 -*-
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from django.contrib.auth.forms import AuthenticationForm


class AccountSingleton(object):
    """
    单例基类
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Account(AccountSingleton):
    def login(self, request, template_name='login/login.html', authentication_form=AuthenticationForm):
        """
        :param authentication_form:
        :param template_name:
        :type request: HttpRequest
        """
        if request.method == "POST":
            form = authentication_form(request, data=request.POST)
            if form.is_valid():
                return self.login_success_response()
        else:
            form = authentication_form(request)
        context = {

        }
        resp = TemplateResponse(request, template_name, context)
        return resp
