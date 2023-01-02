from .models import Project
from rest_framework import serializers

from django.core.exceptions import ObjectDoesNotExist


class ProjectSerializer(serializers.ModelSerializer):
    project_user = serializers.CharField(source="created_by.name",read_only=True)
    class Meta:
        model = Project
        fields = '__all__'


class GetProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    assign_to = serializers.SerializerMethodField()
    def get_created_by(self, obj):
        try:
            return obj.created_by.name
        except Exception as e:
            return None
    def get_assign_to(self, obj):
        try:
            return obj.assign_to.name
        except Exception as e:
            return None

    class Meta:
        model = Project
        fields = '__all__'
