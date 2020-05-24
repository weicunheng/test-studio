# -*- coding: utf-8 -*-
from django.urls import path, include
from django.conf.urls import url
from studioapps.project import views

urlpatterns = [
    # 项目相关接口
    path('', include([
        path('', views.ProjectsAPIView.as_view(), name="projects"),  # 项目列表
        path('<int:project_id>/', views.ProjectAPIView.as_view(), name="project"),  # 项目详情
        path('environ/', views.ProjectEnvironmentAPIView.as_view(), name="project_environ"),  # 项目域名配置

        # 项目成员管理
        path('<int:project_id>/members/', views.ProjectMembersAPIView.as_view(), name="project_members"),

        # 项目域名管理
        path('<int:project_id>/domain/', views.ProjectDomainAPIView.as_view(), name="project_domain")
    ])),

]
