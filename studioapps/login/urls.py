# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from studioapps.login import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = "login"

urlpatterns = [
    url(r"^$", views.LoginView.as_view(), name="login_view"),
    url(r"^api-token-auth/$", views.APILoginView.as_view(), name="api-token-auth"),
]
