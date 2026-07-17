from rest_framework import serializers
from .models import (
    UserProfile,
    Teacher,
    Student,
    Links,
    Category,
    Course,
    Lesson,
    Assignment,
    Exam,
    Question,
    Answers,
    Certificate,
    CourseReview,
    Cart,
    CartItem,
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "full_name", "profile_picture", "role"]


class TeacherSerializer(serializers.ModelSerializer):
    teacher = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ["teacher", "experience", "teacher_role", "bio"]


class StudentSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ["id", "student", "student_role"]


class LinksSerializer(serializers.ModelSerializer):
    links_student = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Links
        fields = ["id", "links_student","links_url"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]


class CourseSerializer(serializers.ModelSerializer):
    course_cartegory = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ["course_cartegory","course_name","description"]


class CourseDetailSerializer(serializers.ModelSerializer):
    course_category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ["course_category","course_name","description","level","price","created_by","created_at","updated_at"]


class LessonSerializer(serializers.ModelSerializer):
    lesson_course = CourseSerializer(many=True,read_only=True)
    class Meta:
        model = Lesson
        fields = ["name_lesson","lesson_course","content","video_url"]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

