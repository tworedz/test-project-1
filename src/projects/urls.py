from django.urls import path

from projects.views import ProjectListAPIView, ProjectRetrieveAPIView

urlpatterns = [
    path("", ProjectListAPIView.as_view(), name="project-list"),
    path("<int:pk>/", ProjectRetrieveAPIView.as_view(), name="project-retrieve"),
]
