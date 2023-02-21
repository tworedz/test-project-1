from django.db import models


class Department(models.Model):
    """Department"""

    name = models.CharField("name", max_length=100)

    owner = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        verbose_name="owner",
        related_name="departments",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"

    def __str__(self) -> str:
        return self.name
