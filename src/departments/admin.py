from django.contrib import admin

from departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    search_fields = ("name",)
