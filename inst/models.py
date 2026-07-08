from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES_ROLE(
    ('Client', 'Client'),
    ('Teacher', 'Teacher'),
    ('Admin', 'Admin'),
)

CHOICES_LEVEL(
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('advanced', 'advanced')
)

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=35 , unique=True)
    profile_picture = models.ImageField(upload_to='profile_image', null=True, blank=True)
    role = models.CharField(max_length=5,choices=CHOICES_ROLE)


class Teacher(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default=1)
    teacher_role = models.CharField(max_length=5, choices=CHOICES_ROLE, default='Teacher')
    bio = models.TextField()


class Student(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    student_role = models.CharField(max_length=5, choices=CHOICES_ROLE, default='Client')


class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    links_url = models.URLField()


class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=25)
    description = models.TextField()
    level = models.CharField(max_length=15, choices=CHOICES_LEVEL,)
    price = models.IntegerField()
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)