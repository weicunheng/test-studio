# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from studioapps.login.decorators import login_exempt


class LoginExemptMixin(object):
    @method_decorator(login_exempt)
    def dispatch(self, *args, **kwargs):
        return super(LoginExemptMixin, self).dispatch(*args, **kwargs)
