from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES_ROLE(
    ('Client', 'Client'),
    ('Teacher', 'Teacher'),
    ('Admin', 'Admin'),
)

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=25)
    profile_picture = models.ImageField(upload_to='profile_image', null=True, blank=True)
    role = models.CharField(max_length=5,choices=CHOICES_ROLE)


class Teacher(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    experience = models.IntegerField()
    teacher_role = models.CharField(max_length=5, choices=CHOICES_ROLE, default='Teacher')
    bio = models.TextField()


class Student(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    student_role = models.CharField(max_length=5, choices=CHOICES_ROLE, default='Client')


class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField(blank=True, null=True)


class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)