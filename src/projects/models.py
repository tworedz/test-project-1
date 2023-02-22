from django.db import models


class Project(models.Model):
    """project"""

    name = models.CharField("name", max_length=100)

    owner = models.ForeignKey(
        "employees.Employee",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    employees = models.ManyToManyField("employees.Employee", related_name="projects")

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self) -> str:
        return self.name
