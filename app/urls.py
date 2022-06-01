from django.contrib import admin
from django.urls import path
from .views import CourseView, CourseDetailView

urlpatterns = [
    path('course/<int:pk>', CourseDetailView.as_view()),
    path('course/', CourseView.as_view())
]
