# -*- coding: utf-8 -*-
from django.urls import path, include
from django.conf.urls import url
from studioapps.project import views

urlpatterns = [
    # 项目相关接口
    path('projects/', include([
        path('', views.ProjectsAPIView.as_view(), name="projects"),
        path('<int:project_id>/', views.ProjectAPIView.as_view(), name="project"),
        path('environ/', views.ProjectEnvironmentAPIView.as_view(), name="project_environ"),
    ])),

]
