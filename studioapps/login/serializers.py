# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import Serializer, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(**kwargs)


class LoginTokenSerializer(Serializer):
    username_field = User.USERNAME_FIELD

    def __init__(self, *args, **kwargs):

        super(LoginTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def object(self):
        return self.validated_data

    def validate(self, attrs):

        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        if all(credentials):
            user = authenticate(**credentials)
            if user:
                if user.is_active:
                    token = RefreshToken.for_user(user)
                    return {
                        "refresh": str(token),
                        "token": str(token.access_token),
                        "user": user,
                    }
                else:
                    raise Exception("AUTHENTICATION_FAILED")
            else:
                raise Exception("AUTHENTICATION_FAILED")
        else:
            raise Exception("ERROR_USERNAME_PASSWORD_CANNOT_BE_EMPTY")
