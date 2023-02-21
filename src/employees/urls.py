from django.urls import path

from employees.views import EmployeeListAPIView, EmployeeRetrieveUpdateAPIView

urlpatterns = [
    path("", EmployeeListAPIView.as_view(), name="employee-list-create"),
    path(
        "<int:pk>/",
        EmployeeRetrieveUpdateAPIView.as_view(),
        name="employee-retrieve-update",
    ),
]
