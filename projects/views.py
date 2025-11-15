from django.shortcuts import render
from rest_framework import viewsets, permissions
from projects.models import Project
from projects.serializers import ProjectSerializer


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]