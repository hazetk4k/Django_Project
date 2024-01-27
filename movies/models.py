from django.db import models


# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=20, blank=False)
    salary = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} {self.second_name}"
