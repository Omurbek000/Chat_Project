from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users',UserProfileViewSet)
router.register('teacher',TeacherViewSet)
router.register('student',StudentViewSet)
router.register('links',LinksViewSet)
router.register('category',CategoryViewSet)
router.register('course',CourseViewSet)
router.register('lesson',LessonViewSet)
router.register('assignment',AssignmentViewSet)
router.register('exem',ExamViewSet)
router.register('question',QuestionViewSet)
router.register('answers',AnswersViewSet)
router.register('certificate',CertificateViewSet)
router.register('course_review',CourseReviewViewSet)
router.register('cart',CartViewSet)
router.register('cart_item',CartItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]