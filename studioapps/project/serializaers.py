# -*- coding: utf-8 -*-
from rest_framework import serializers

from studioapps.project.models import Project, ProjectEnvironment
from studioapps.project.constants import PERMISSION_TYPE_DICT


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectEnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEnvironment
        fields = "__all__"


class ProjectMembersSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return {
            'name': instance.name,
            'role_id': instance.permissionType,
            'role_text': PERMISSION_TYPE_DICT[instance.permissionType],
            'contact': instance.profile.contact,
            'email': instance.profile.email
        }
