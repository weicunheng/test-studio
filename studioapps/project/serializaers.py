# -*- coding: utf-8 -*-
from rest_framework import serializers

from studioapps.project.models import Project, ProjectEnvironment


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class ProjectEnvironmentSerializer(serializers.ModelSerializer):


    class Meta:
        model = ProjectEnvironment
        fields = "__all__"
