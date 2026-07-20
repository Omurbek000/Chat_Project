from django_filters import FilterSet, NumberFilter, CharFilter
from .models import (
    UserProfile, Teacher, Student, Course, Lesson, Exam, Certificate
)


class UserProfileFilter(FilterSet):
    class Meta:
        model = UserProfile
        fields = {
            'full_name': ['exact', 'icontains'],
            'role': ['exact'],
        }


class TeacherFilter(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'teacher_role': ['exact'],
            'experience': ['gt', 'gte', 'lt', 'lte'],
        }


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'student': ['exact'],
            'student_role': ['exact'],
        }


class CourseFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    category_name = CharFilter(
        field_name='category__category_name', lookup_expr='icontains'
    )

    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'course_name': ['exact', 'icontains'],
            'level': ['exact'],
            'created_by': ['exact'],
            'created_at': ['exact', 'year', 'month'],
        }


class LessonFilter(FilterSet):
    class Meta:
        model = Lesson
        fields = {
            'course': ['exact'],
            'name_lesson': ['exact', 'icontains'],
        }




class ExamFilter(FilterSet):
    class Meta:
        model = Exam
        fields = {
            'course': ['exact'],
            'passing_score': ['gt', 'gte', 'lt', 'lte'],
            'duration': ['gt', 'gte', 'lt', 'lte'],
        }


class CertificateFilter(FilterSet):
    class Meta:
        model = Certificate
        fields = {
            'student': ['exact'],
            'course': ['exact'],
        }



