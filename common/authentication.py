# -*- coding: utf-8 -*-
from rest_framework_simplejwt.tokens import Token
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class MyAccessToken(Token):
    token_type = 'access'
    lifetime = api_settings.ACCESS_TOKEN_LIFETIME

    def __init__(self, token=None, verify=False):
        super(MyAccessToken, self).__init__(token, verify=False)


class MyJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        """
        Validates an encoded JSON web token and returns a validated token
        wrapper object.
        """
        messages = []
        try:
            return MyAccessToken(raw_token)
        except TokenError as e:
            messages.append({'token_class': MyAccessToken.__name__,
                             'token_type': MyAccessToken.token_type,
                             'message': e.args[0]})
        raise InvalidToken({
            'detail': _('Given token not valid for any token type'),
            'messages': messages,
        })
