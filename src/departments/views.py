from django.db import models
from rest_framework import generics
from rest_framework.permissions import AllowAny

from departments.models import Department
from departments.serializers import DepartmentSerializer


class DepartmentListAPIView(generics.ListAPIView):
    queryset = (
        Department.objects.prefetch_related("employees")
        .annotate(total_salary=models.Sum("employees__salary"))
        .all()
    )
    serializer_class = DepartmentSerializer
    pagination_class = None
    permission_classes = (AllowAny,)
