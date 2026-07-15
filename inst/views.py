from rest_framework import viewsets
from .models import UserProfile, Teacher,Student,Links,Category, Course,Lesson,Assignment,Exam,Question,Answers,Certificate,CourseReview,Cart,CartItem
from .serializers import UserProfileSerializer,TeacherSerializer,StudentSerializer, LinksSerializer, CategorySerializer, CourseSerializer, LessonSerializer, AssignmentSerializer, ExamSerializer, QuestionSerializer, AnswersSerializer,CertificateSerializer,CourseReviewSerializer,CartSerializer, CartItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CourseFilter
from rest_framework import permissions
from .permissions import CheckOwner, CheckUserOwner, CheckCourseOwner




class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =StudentSerializer


class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links .objects.all()
    serializer_class = LinksSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price']


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CourseReviewViewSet(viewsets.ModelViewSet):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
