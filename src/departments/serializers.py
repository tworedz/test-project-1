from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from departments.models import Department
from employees.serializers import EmployeeSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()
    employee_count = serializers.SerializerMethodField()
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "owner",
            "employee_count",
            "total_salary",
        )

    @extend_schema_field(OpenApiTypes.INT)
    def get_employee_count(self, obj: Department) -> int:
        return len(obj.employees.all())

    @extend_schema_field(OpenApiTypes.INT)
    def get_total_salary(self, obj: Department) -> int:
        return obj.total_salary or 0
