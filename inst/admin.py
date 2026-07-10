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
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


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