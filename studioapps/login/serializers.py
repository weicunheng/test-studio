# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import Serializer, ValidationError
from rest_framework_jwt.compat import get_username_field, PasswordField
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginTokenSerializer(Serializer):
    def __init__(self, *args, **kwargs):

        super(LoginTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    @property
    def username_field(self):
        return get_username_field()

    @property
    def object(self):
        return self.validated_data

    def validate(self, attrs):
        print("atts", attrs)

        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        if all(credentials):
            user = authenticate(**credentials)
            if user:
                if user.is_active:
                    payload = jwt_payload_handler(user)
                    return {
                        "token": jwt_encode_handler(payload),
                        "user": user,
                    }
                else:
                    raise ValidationError("当前用户不可用")
            else:
                raise ValidationError("用户认证失败")
        else:
            raise ValidationError("用户名密码不能为空")
