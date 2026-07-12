from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES_ROLE = (
    ("Client", "Client"),
    ("Teacher", "Teacher"),
    ("Admin", "Admin"),
)

CHOICES_LEVEL = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("advanced", "advanced"),
)


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=35)
    profile_picture = models.ImageField(
        upload_to="profile_image/", null=True, blank=True
    )
    role = models.CharField(max_length=20, choices=CHOICES_ROLE)

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    teacher = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='teacher')
    experience = models.PositiveIntegerField(default=1)
    teacher_role = models.CharField(
        max_length=10, choices=CHOICES_ROLE, default="Teacher"
    )
    bio = models.TextField()

    def __str__(self):
        return f"{self.teacher.full_name} ({self.teacher_role})"


class Student(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='student')
    student_role = models.CharField(
        max_length=10, choices=CHOICES_ROLE, default="Client"
    )

    def __str__(self):
        return f"{self.student.full_name} ({self.student_role})"


class Links(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='links_student')
    links_url = models.URLField()

    def __str__(self):
        return f"{self.student} - {self.links_url}"


class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_cartegory')
    course_name = models.CharField(max_length=25)
    description = models.TextField()
    level = models.CharField(
        max_length=15,
        choices=CHOICES_LEVEL,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='lesson_course')

    def __str__(self):
        return f"{self.course.course_name} - {self.name_lesson}"


class Assignment(models.Model):
    name_assignment = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.course.course_name} - {self.name_assignment}"


class Exam(models.Model):
    name_exam = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.PositiveIntegerField()
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.course.course_name} - {self.name_exam}"


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name_question = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.name_question


class Answers(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    true_answers = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.URLField()

    def __str__(self):
        return f"{self.student} - {self.course.course_name}"


class CourseReview(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.course.course_name} ({self.rating})"


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.full_name}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart} - {self.course.course_name}"


class Chat(models.Model):
    people = models.ManyToManyField(UserProfile)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="message_images/", null=True, blank=True)
    video = models.FileField(upload_to="messeges_video/", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.full_name}: {self.text[:30]}"
