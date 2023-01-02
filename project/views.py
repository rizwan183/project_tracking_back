from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer, GetProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.utils import timezone
import datetime
from django.http import Http404
from rest_framework.permissions import IsAuthenticated


class ProjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid=None):
        print("is admin", request.user.is_admin)
        if uuid is None:
            project = Project.objects.filter(created_by=request.user)
            print(project)
            serializer = GetProjectSerializer(project[::-1], many=True)
            print(project)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            project = Project.objects.get(uuid=uuid)
            serializer = GetProjectSerializer(project, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.user.is_admin)

        data = request.data
        print("data", data)
        keys = list(data.keys())
        print("keys", keys)
        data.update({"created_by": request.user.id})
        if request.user.is_admin:
            if "assign_to" not in keys:
                data.update({"assign_to": request.user.id})
            else:
                pass
        else:
            data.update({"assign_to": request.user.id})
            print("updated dataaaaa", data)
            # data.update({"assign_to": request.user.id})
        print("data", data)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        print("hello")
        project = Project.objects.get(uuid=pk)
        print("project", project)
        serializer = GetProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            project = project = Project.objects.get(uuid=pk)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
