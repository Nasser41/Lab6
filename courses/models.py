from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    registration_number = models.CharField(max_length=255, unique=True)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
