# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from studioapps.account import views

app_name = "account"

urlpatterns = [
    url(r'^user/', include([
    ])),
]