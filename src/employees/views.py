from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeUpdateSerializer


class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ("last_name",)
    filterset_fields = ("department__id",)


class EmployeeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeUpdateSerializer
