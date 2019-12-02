# -*- coding: utf-8 -*-
from rest_framework import serializers

from studioapps.project.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        pass



    class Meta:
        model = Project
        fields = "__all__"
