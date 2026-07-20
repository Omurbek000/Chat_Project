from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (
    UserProfile, Teacher, Student, Links, Category, Course,
    Lesson, Assignment, Exam, Question, Answers,
    Certificate, CourseReview, Cart, CartItem
)
from .serializers import (
    UserProfileListSerializer, UserProfileDetailSerializer,
    TeacherListSerializer, TeacherDetailSerializer,
    StudentListSerializer, StudentDetailSerializer,
    LinksListSerializer, LinksDetailSerializer,
    CategoryListSerializer, CategoryDetailSerializer,
    CourseListSerializer, CourseDetailSerializer,
    LessonListSerializer, LessonDetailSerializer,
    AssignmentListSerializer, AssignmentDetailSerializer,
    ExamListSerializer, ExamDetailSerializer,
    QuestionListSerializer, QuestionDetailSerializer,
    AnswersListSerializer, AnswersDetailSerializer,
    CertificateListSerializer, CertificateDetailSerializer,
    CourseReviewListSerializer, CourseReviewDetailSerializer,
    CartListSerializer, CartDetailSerializer,
    CartItemListSerializer, CartItemDetailSerializer,
    RegisterSerializer, TeacherRegisterSerializer, StudentRegisterSerializer,
    LoginSerializer, LogoutSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import CourseFilter
from rest_framework import permissions
from .permissions import IsOwner, IsStudent, IsCourseOwner


# ==================== AUTH VIEWS ====================

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class TeacherRegisterView(generics.CreateAPIView):
    serializer_class = TeacherRegisterSerializer


class StudentRegisterView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer


class CustomLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': user.full_name,
                'role': user.role,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Вы вышли из системы.'}, status=status.HTTP_205_RESET_CONTENT)


# ==================== USER PROFILE ====================

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# ==================== TEACHER ====================

class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    permission_classes = [permissions.AllowAny]


class TeacherDetailAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer
    permission_classes = [permissions.AllowAny]


# ==================== STUDENT ====================

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudentDetailAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# ==================== LINKS ====================

class LinksListAPIView(generics.ListAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksListSerializer
    permission_classes = [permissions.IsAuthenticated]


class LinksDetailAPIView(generics.RetrieveAPIView):
    queryset = Links.objects.all()
    serializer_class = LinksDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# ==================== CATEGORY ====================

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [permissions.AllowAny]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.AllowAny]


# ==================== COURSE ====================

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price']
    permission_classes = [permissions.AllowAny]


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [permissions.AllowAny]


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsOwner]


class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsCourseOwner]


class CourseDeleteAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsCourseOwner]


# ==================== LESSON ====================

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [permissions.AllowAny]


class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [permissions.AllowAny]


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsOwner]


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsOwner]


# ==================== ASSIGNMENT ====================

class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer
    permission_classes = [permissions.AllowAny]


class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer
    permission_classes = [permissions.AllowAny]


class AssignmentCreateAPIView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer
    permission_classes = [IsOwner]


class AssignmentUpdateAPIView(generics.UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer
    permission_classes = [IsOwner]


class AssignmentDeleteAPIView(generics.DestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer
    permission_classes = [IsOwner]


# ==================== EXAM ====================

class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer
    permission_classes = [permissions.AllowAny]


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer
    permission_classes = [permissions.AllowAny]


class ExamCreateAPIView(generics.CreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer
    permission_classes = [IsOwner]


class ExamUpdateAPIView(generics.UpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer
    permission_classes = [IsOwner]


class ExamDeleteAPIView(generics.DestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer
    permission_classes = [IsOwner]


# ==================== QUESTION ====================

class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    permission_classes = [permissions.AllowAny]


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [permissions.AllowAny]


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsOwner]


class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsOwner]


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    permission_classes = [IsOwner]


# ==================== ANSWERS ====================

class AnswersListAPIView(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersListSerializer
    permission_classes = [permissions.AllowAny]


class AnswersDetailAPIView(generics.RetrieveAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersDetailSerializer
    permission_classes = [permissions.AllowAny]


class AnswersCreateAPIView(generics.CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersDetailSerializer
    permission_classes = [IsOwner]


class AnswersUpdateAPIView(generics.UpdateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersDetailSerializer
    permission_classes = [IsOwner]


class AnswersDeleteAPIView(generics.DestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersDetailSerializer
    permission_classes = [IsOwner]


# ==================== CERTIFICATE ====================

class CertificateListAPIView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertificateDetailAPIView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


# ==================== COURSE REVIEW ====================

class CourseReviewListAPIView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewListSerializer
    permission_classes = [permissions.AllowAny]


class CourseReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [permissions.AllowAny]


class CourseReviewCreateAPIView(generics.CreateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [IsStudent]


class CourseReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [IsStudent]


class CourseReviewDeleteAPIView(generics.DestroyAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewDetailSerializer
    permission_classes = [IsStudent]


# ==================== CART ====================

class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [IsStudent]


class CartDetailAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [IsStudent]


class CartCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer
    permission_classes = [IsStudent]


# ==================== CART ITEM ====================

class CartItemListAPIView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemListSerializer
    permission_classes = [IsStudent]


class CartItemDetailAPIView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsStudent]


class CartItemCreateAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializer
    permission_classes = [IsStudent]
