from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_select_related = ("department",)
    list_display = ("first_name", "last_name", "department")
