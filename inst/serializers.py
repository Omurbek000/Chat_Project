from rest_framework import serializers
from .models import (
    UserProfile, Teacher, Student, Links, Category, Course,
    Lesson, Assignment, Exam, Question, Answers,
    Certificate, CourseReview, Cart, CartItem
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# ==================== AUTH SERIALIZERS ====================

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password2', 'full_name', 'role']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'id': instance.id,
                'username': instance.username,
                'email': instance.email,
                'full_name': instance.full_name,
                'role': instance.role,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    bio = serializers.CharField()
    experience = serializers.IntegerField(default=1)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password2', 'full_name', 'bio', 'experience']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        bio = validated_data.pop('bio')
        experience = validated_data.pop('experience')
        user = UserProfile.objects.create_user(
            **validated_data,
            role='Teacher'
        )
        Teacher.objects.create(
            teacher=user,
            bio=bio,
            experience=experience,
            teacher_role='Teacher'
        )
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'id': instance.id,
                'username': instance.username,
                'email': instance.email,
                'full_name': instance.full_name,
                'role': instance.role,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class StudentRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'password2', 'full_name']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = UserProfile.objects.create_user(
            **validated_data,
            role='Client'
        )
        Student.objects.create(
            student=user,
            student_role='Client'
        )
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'id': instance.id,
                'username': instance.username,
                'email': instance.email,
                'full_name': instance.full_name,
                'role': instance.role,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'id': instance.id,
                'username': instance.username,
                'email': instance.email,
                'full_name': instance.full_name,
                'role': instance.role,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            raise serializers.ValidationError({'detail': 'Недействительный или уже отозванный токен'})


# ==================== USER PROFILE ====================

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "full_name", "profile_picture", "role"]


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "full_name", "profile_picture", "role"]


# ==================== TEACHER ====================

class TeacherListSerializer(serializers.ModelSerializer):
    teacher = UserProfileListSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ["id", "teacher", "experience", "teacher_role"]


class TeacherDetailSerializer(serializers.ModelSerializer):
    teacher = UserProfileDetailSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ["id", "teacher", "experience", "teacher_role", "bio"]


# ==================== STUDENT ====================

class StudentListSerializer(serializers.ModelSerializer):
    student = UserProfileListSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "student", "student_role"]


class StudentDetailSerializer(serializers.ModelSerializer):
    student = UserProfileDetailSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ["id", "student", "student_role"]


# ==================== LINKS ====================

class LinksListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer(read_only=True)

    class Meta:
        model = Links
        fields = ["id", "student", "links_url"]


class LinksDetailSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(read_only=True)

    class Meta:
        model = Links
        fields = ["id", "student", "links_url"]


# ==================== CATEGORY ====================

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]


# ==================== COURSE ====================

class CourseListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    created_by = TeacherListSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "course_name", "level", "price", "category", "created_by"]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer(read_only=True)
    created_by = TeacherDetailSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ["id", "course_name", "description", "level", "price", "category", "created_by", "created_at", "updated_at"]


# ==================== LESSON ====================

class LessonListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "name_lesson", "course"]


class LessonDetailSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "name_lesson", "course", "video_url", "content"]


# ==================== ASSIGNMENT ====================

class AssignmentListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "name_assignment", "course", "due_date"]


class AssignmentDetailSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer(read_only=True)
    students = StudentListSerializer(many=True, read_only=True)

    class Meta:
        model = Assignment
        fields = ["id", "name_assignment", "description", "due_date", "course", "students"]


# ==================== EXAM ====================

class ExamListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = ["id", "name_exam", "course"]


class ExamDetailSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = ["id", "name_exam", "course", "passing_score", "duration"]


# ==================== QUESTION ====================

class QuestionListSerializer(serializers.ModelSerializer):
    exam = ExamListSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "name_question", "exam"]


class QuestionDetailSerializer(serializers.ModelSerializer):
    exam = ExamDetailSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "name_question", "exam", "text"]


# ==================== ANSWERS ====================

class AnswersListSerializer(serializers.ModelSerializer):
    questions = QuestionListSerializer(read_only=True)

    class Meta:
        model = Answers
        fields = ["id", "questions", "answer_text"]


class AnswersDetailSerializer(serializers.ModelSerializer):
    questions = QuestionDetailSerializer(read_only=True)

    class Meta:
        model = Answers
        fields = ["id", "questions", "answer_text", "true_answers"]


# ==================== CERTIFICATE ====================

class CertificateListSerializer(serializers.ModelSerializer):
    student = StudentListSerializer(read_only=True)
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = ["id", "student", "course", "issued_at"]


class CertificateDetailSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer(read_only=True)
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = ["id", "student", "course", "issued_at", "certificate_url"]


# ==================== COURSE REVIEW ====================

class CourseReviewListSerializer(serializers.ModelSerializer):
    user = StudentListSerializer(read_only=True)
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = CourseReview
        fields = ["id", "user", "course", "rating"]


class CourseReviewDetailSerializer(serializers.ModelSerializer):
    user = StudentDetailSerializer(read_only=True)
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = CourseReview
        fields = ["id", "user", "course", "rating", "comment"]


# ==================== CART ====================

class CartListSerializer(serializers.ModelSerializer):
    user = UserProfileListSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "created_date"]


class CartDetailSerializer(serializers.ModelSerializer):
    user = UserProfileDetailSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "user", "created_date"]


# ==================== CART ITEM ====================

class CartItemListSerializer(serializers.ModelSerializer):
    cart = CartListSerializer(read_only=True)
    course = CourseListSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "course"]


class CartItemDetailSerializer(serializers.ModelSerializer):
    cart = CartDetailSerializer(read_only=True)
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "course"]
