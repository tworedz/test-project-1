from rest_framework import serializers

from employees.serializers import EmployeeInfoSerializer, EmployeeSerializer
from projects.models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "owner",
        )


class ProjectSerializer(serializers.ModelSerializer):
    owner = EmployeeSerializer()
    employees = EmployeeInfoSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "owner",
            "employees",
        )
