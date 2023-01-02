from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TaskSerializer
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
from .models import Task


# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, uuid=None):
        print("is admin", request.user.is_admin)
        if uuid is None:
            project = Task.objects.filter(created_by=request.user)
            print(project)
            serializer = TaskSerializer(project, many=True)
            print(project)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            project = Task.objects.get(uuid=uuid)
            serializer = TaskSerializer(project, many=True)
            print(project)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.user.is_admin)
        print(request.data)
        data = request.data
        data.update({"user": request.user.id})
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
