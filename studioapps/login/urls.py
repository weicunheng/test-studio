# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from studioapps.login import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "login"

urlpatterns = [
    url(r"^login/$", views.APILoginView.as_view(), name="api-token-auth"),
    url(r"^refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]
