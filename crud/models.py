from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"Student {self.name}"
