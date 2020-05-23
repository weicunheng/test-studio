# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from studioapps.login import views

app_name = "login"

urlpatterns = [
    # url(r"^$", views.LoginView.as_view(), name="login_view"),
    url(r"^$", views.APILoginView.as_view(), name="api-token-auth"),
]
