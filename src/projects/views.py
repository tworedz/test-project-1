from rest_framework import generics

from projects.models import Project
from projects.serializers import ProjectListSerializer, ProjectSerializer


class ProjectListAPIView(generics.ListAPIView):
    queryset = (
        Project.objects.prefetch_related("employees").select_related("owner").all()
    )
    serializer_class = ProjectListSerializer


class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = (
        Project.objects.prefetch_related("employees").select_related("owner").all()
    )
    serializer_class = ProjectSerializer
