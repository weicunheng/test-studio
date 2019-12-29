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
        projects = models.Project.objects.filter(creater=request.user)
        return Response(self.serializer_class(projects).data)

    def post(self, request):
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
        try:
            project = models.Project.objects.get(pk=project_id)
            return Response(self.serializer_class(project).data)

        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")

    def put(self, request, project_id):
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
        try:
            project = models.Project.objects.get(pk=project_id)
            project.is_delete = True
            project.save()
            return Response()

        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")


class ProjectEnvironmentAPIView(BaseAPIView):
    serializer_class = serializaers.ProjectEnvironmentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            project = models.Project.objects.get(pk=serializer.validated_data['project'])
            models.ProjectEnvironment.objects.create(project=project, environ=serializer.validated_data['environ'],
                                                     domain=serializer.validated_data['domain'])

        except models.Project.DoesNotExist:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")
        except Exception as e:
            raise NotFound("ERROR_NOT_EXIST_PROJECT")

        return Response('OK')


class ProjectUserAPIView(BaseAPIView):

    def get(self, request):
        pass

    def put(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass