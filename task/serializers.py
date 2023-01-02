from .models import Task
from rest_framework import serializers

from django.core.exceptions import ObjectDoesNotExist


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    assign_to = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()

    def get_project(self, obj):
        try:
            return obj.created_by.name
        except ObjectDoesNotExist:
            # the day object doesn't have any
            # pet associated, so return None
            return None

    def get_created_by(self, obj):
        try:
            return obj.created_by.name
        except ObjectDoesNotExist:
            # the day object doesn't have any
            # pet associated, so return None
            return None

    def get_assign_to(self, obj):
        try:
            return obj.assign_to.name
        except ObjectDoesNotExist:
            # the day object doesn't have any
            # pet associated, so return None
            return None

    class Meta:
        model = Task
        fields = '__all__'
