# -*- coding: utf-8 -*-
from django.urls import path, include
from django.conf.urls import url
from studioapps.project import views
urlpatterns = [
    url(r'create/$', views.ProjectCreateView.as_view(), name="create_project"),
    url(r'^list/', include([
        url(r"^$", view=views.ProjectListView.as_view(), name="project_list"),
        url(r"^query/$", view=views.ProjectQueryListView.as_view(), name="project_query_list")
    ]))
]