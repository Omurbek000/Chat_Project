from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/teacher/', views.TeacherRegisterView.as_view(), name='register-teacher'),
    path('register/student/', views.StudentRegisterView.as_view(), name='register-student'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # User Profile
    path('users/', views.UserProfileListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserProfileDetailAPIView.as_view(), name='user-detail'),

    # Teacher
    path('teachers/', views.TeacherListAPIView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetailAPIView.as_view(), name='teacher-detail'),

    # Student
    path('students/', views.StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetailAPIView.as_view(), name='student-detail'),

    # Links
    path('links/', views.LinksListAPIView.as_view(), name='links-list'),
    path('links/<int:pk>/', views.LinksDetailAPIView.as_view(), name='links-detail'),

    # Category
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='category-detail'),

    # Course
    path('courses/', views.CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course-detail'),
    path('courses/create/', views.CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', views.CourseUpdateAPIView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteAPIView.as_view(), name='course-delete'),

    # Lesson
    path('lessons/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', views.LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lessons/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/update/', views.LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', views.LessonDeleteAPIView.as_view(), name='lesson-delete'),

    # Assignment
    path('assignments/', views.AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', views.AssignmentDetailAPIView.as_view(), name='assignment-detail'),
    path('assignments/create/', views.AssignmentCreateAPIView.as_view(), name='assignment-create'),
    path('assignments/<int:pk>/update/', views.AssignmentUpdateAPIView.as_view(), name='assignment-update'),
    path('assignments/<int:pk>/delete/', views.AssignmentDeleteAPIView.as_view(), name='assignment-delete'),

    # Exam
    path('exams/', views.ExamListAPIView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', views.ExamDetailAPIView.as_view(), name='exam-detail'),
    path('exams/create/', views.ExamCreateAPIView.as_view(), name='exam-create'),
    path('exams/<int:pk>/update/', views.ExamUpdateAPIView.as_view(), name='exam-update'),
    path('exams/<int:pk>/delete/', views.ExamDeleteAPIView.as_view(), name='exam-delete'),

    # Question
    path('questions/', views.QuestionListAPIView.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetailAPIView.as_view(), name='question-detail'),
    path('questions/create/', views.QuestionCreateAPIView.as_view(), name='question-create'),
    path('questions/<int:pk>/update/', views.QuestionUpdateAPIView.as_view(), name='question-update'),
    path('questions/<int:pk>/delete/', views.QuestionDeleteAPIView.as_view(), name='question-delete'),

    # Answers
    path('answers/', views.AnswersListAPIView.as_view(), name='answers-list'),
    path('answers/<int:pk>/', views.AnswersDetailAPIView.as_view(), name='answers-detail'),
    path('answers/create/', views.AnswersCreateAPIView.as_view(), name='answers-create'),
    path('answers/<int:pk>/update/', views.AnswersUpdateAPIView.as_view(), name='answers-update'),
    path('answers/<int:pk>/delete/', views.AnswersDeleteAPIView.as_view(), name='answers-delete'),

    # Certificate
    path('certificates/', views.CertificateListAPIView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', views.CertificateDetailAPIView.as_view(), name='certificate-detail'),

    # Course Review
    path('reviews/', views.CourseReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.CourseReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/create/', views.CourseReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/update/', views.CourseReviewUpdateAPIView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', views.CourseReviewDeleteAPIView.as_view(), name='review-delete'),

    # Cart
    path('cart/', views.CartListAPIView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', views.CartDetailAPIView.as_view(), name='cart-detail'),
    path('cart/create/', views.CartCreateAPIView.as_view(), name='cart-create'),

    # Cart Item
    path('cart-items/', views.CartItemListAPIView.as_view(), name='cartitem-list'),
    path('cart-items/<int:pk>/', views.CartItemDetailAPIView.as_view(), name='cartitem-detail'),
    path('cart-items/create/', views.CartItemCreateAPIView.as_view(), name='cartitem-create'),
]
