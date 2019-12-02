# -*- coding: utf-8 -*-

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


def client_action_wrapper(action):
    def wrapper_method(self, *args, **kwargs):
        if self.view_name is None:
            raise ValueError('Must give value for `view_name` property')

        reverse_args = kwargs.pop('reverse_args', tuple())
        reverse_kwargs = kwargs.pop('reverse_kwargs', dict())
        query_string = kwargs.pop('query_string', None)

        url = reverse(self.view_name, args=reverse_args, kwargs=reverse_kwargs)
        if query_string is not None:
            url = url + '?{0}'.format(query_string)

        return getattr(self.client, action)(url, *args, **kwargs)

    return wrapper_method


class APIViewTestCase(TestCase):
    client_class = APIClient

    def authenticate_with_token(self, type, token):
        self.client.credentials(HTTP_AUTHORIZATION='{} {}'.format(type, token))

    view_name = None

    view_post = client_action_wrapper('post')
    view_get = client_action_wrapper('get')
    view_put = client_action_wrapper('put')
