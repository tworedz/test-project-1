from django.db import models


class Employee(models.Model):
    """Employee"""

    first_name = models.CharField("first name", max_length=100)
    last_name = models.CharField("last name", max_length=100, db_index=True)
    salary = models.PositiveIntegerField("salary")
    photo = models.ImageField("photo", null=True, blank=True)
    age = models.PositiveIntegerField("age")

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        verbose_name="department",
        related_name="employees",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"
        unique_together = ("id", "department")
        ordering = ("-id",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
