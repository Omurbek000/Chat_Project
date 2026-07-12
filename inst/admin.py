from django.contrib import admin
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
    Chat,
    Message,
)
from modeltranslation.admin import (
    TranslationAdmin,
    # TranslationInlineModelAdmin,
    TranslationTabularInline,
)


class TranslationMediaMixin:
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


class LinksInline(admin.TabularInline):
    model = Links
    extra = 1


class LessonInline(TranslationMediaMixin, TranslationTabularInline):
    model = Lesson
    extra = 1
    fields = ("name_lesson", "video_url", "content")


class AssignmentInline(TranslationMediaMixin, TranslationTabularInline):
    model = Assignment
    extra = 1
    fields = ("name_assignment", "description", "due_date", "students")
    filter_horizontal = ("students",)


class ExamInline(TranslationMediaMixin, TranslationTabularInline):
    model = Exam
    extra = 1
    fields = ("name_exam", "passing_score", "duration")


class QuestionInline(TranslationMediaMixin, TranslationTabularInline):
    model = Question
    extra = 1
    fields = ("name_question", "text")


class AnswersInline(TranslationMediaMixin, TranslationTabularInline):
    model = Answers
    extra = 1
    fields = ("answers", "true_answers")


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", "email", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("username", "full_name", "email")


@admin.register(Teacher)
class TeacherAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("teacher", "experience", "teacher_role")
    list_filter = ("teacher_role",)
    search_fields = ("teacher__username", "teacher__full_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student", "student_role")
    list_filter = ("student_role",)
    search_fields = ("student__username", "student__full_name")
    inlines = [LinksInline]


@admin.register(Category)
class CategoryAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)


@admin.register(Course)
class CourseAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = (
        "course_name",
        "category",
        "level",
        "price",
        "created_by",
        "created_at",
    )
    list_filter = ("category", "level")
    search_fields = ("course_name", "description")
    autocomplete_fields = ("category", "created_by")
    inlines = [LessonInline, AssignmentInline, ExamInline]


@admin.register(Lesson)
class LessonAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("name_lesson", "course")
    list_filter = ("course",)
    search_fields = ("name_lesson", "content")


@admin.register(Assignment)
class AssignmentAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("name_assignment", "course", "due_date")
    list_filter = ("course", "due_date")
    search_fields = ("name_assignment", "description")
    filter_horizontal = ("students",)


@admin.register(Exam)
class ExamAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("name_exam", "course", "passing_score", "duration")
    list_filter = ("course",)
    search_fields = ("name_exam",)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("name_question", "exam")
    list_filter = ("exam",)
    search_fields = ("name_question", "text")
    inlines = [AnswersInline]


@admin.register(Answers)
class AnswersAdmin(TranslationMediaMixin, TranslationAdmin):
    list_display = ("questions", "true_answers")
    list_filter = ("true_answers",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "issued_at")
    list_filter = ("course", "issued_at")
    search_fields = ("student__student__username",)


@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "rating")
    list_filter = ("course", "rating")
    search_fields = ("comment",)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_date")
    inlines = [CartItemInline]


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    filter_horizontal = ("people",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("chat", "author", "created_date")
    list_filter = ("chat",)
    search_fields = ("text", "author__username")
