# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.views import APIView
from django.db import transaction
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from common.response import BaseAPIView
from studioapps.project import serializaers

from studioapps.project import models, serializaers


class ProjectsAPIView(BaseAPIView):
    serializer_class = serializaers.ProjectSerializer

    def get(self, request):
        """
        返回项目列表
        """
        projects = models.Project.objects.all().values(
            'name', 'code', 'introduction', 'state', 'tags')
        return Response(projects)

    def post(self, request):
        """
        创建项目
        """
        serializer = self.serializer_class(data=request.data)

        try:
            models.Project.objects.get(name=serializer.validated_data.get("name", ""))
            raise NotFound('ERROR_PROJECT_IS_EXIST')
        except models.Project.DoesNotExist:
            with transaction.atomic():
                if serializer.is_valid(raise_exception=True):
                    project = serializer.save()

                    return Response(self.serializer_class(project).data)


class ProjectAPIView(BaseAPIView):
    serializer_class = serializaers.ProjectSerializer

    def get(self, request, project_id):
        """
        获取项目详细信息
        """
        try:
            project = models.Project.objects.filter(pk=project_id)
            if not project:
                raise NotFound("ERROR_NOT_EXIST_PROJECT")

            return Response(project.values('name', 'code', 'introduction', 'state', 'tags'))
        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")

    def put(self, request, project_id):
        """
        更新项目信息
        """
        try:
            project = models.Project.objects.get(pk=project_id)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.update(project, serializer.validated_data)
            return Response(self.serializer_class(project).data)
        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")

    def delete(self, request, project_id):
        """
        删除项目
        """
        try:
            models.Project.objects.filter(pk=project_id).update(is_delete=True, creator=request.user)
            return Response('OK')
        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")


class ProjectEnvironmentAPIView(BaseAPIView):
    serializer_class = serializaers.ProjectEnvironmentSerializer

    def post(self, request):
        """
        项目不同运行环境域名配置
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        project_id = serializer.validated_data['project']
        environ = serializer.validated_data['environ']
        domain = serializer.validated_data['domain']
        success, msg = models.ProjectEnvironment.create_by_project(project_id=project_id, environ=environ,
                                                                   domain=domain)
        if success:
            return Response('OK')
        else:
            raise NotFound(msg)


class ProjectMembersAPIView(BaseAPIView):
    serializer_class = serializaers.ProjectMembersSerializer

    def get(self, request, project_id):
        project_members = models.ProjectMembers.objects.filter(project_id=project_id)
        memebers = self.serializer_class(project_members, many=True).data
        return Response(memebers)


class ProjectDomainAPIView(BaseAPIView):

    def get(self):
        pass

    def post(self):
        pass
