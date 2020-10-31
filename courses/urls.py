from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # Course
    path('course/create/', CreateCourse.as_view(), name="create_course"),
    path('course/update/<int:pk>/', UpdateCourse.as_view(), name="update_course"),
    path('course/list/', ListCourse.as_view(), name="list_course"),
    path('course/delete/<int:pk>/', DeleteCourse.as_view(), name="delete_course"),
    path('course/get/<int:pk>/', GetCourse.as_view(), name="get_course"),

    # Lesson
    path('lesson/create/', CreateLesson.as_view(), name="create_lesson"),
    path('lesson/update/<int:pk>/', UpdateLesson.as_view(), name="update_lesson"),
    path('lesson/list/', ListLesson.as_view(), name="list_lesson"),
    path('lesson/delete/<int:pk>/', DeleteLesson.as_view(), name="delete_lesson"),
    path('lesson/get/<int:pk>/', GetLesson.as_view(), name="get_lesson"),

    # Question
    path('question/create/', CreateQuestion.as_view(), name="create_question"),
    path('question/update/<int:pk>/', UpdateQuestion.as_view(), name="update_question"),
    path('question/list/', ListQuestion.as_view(), name="list_question"),
    path('question/delete/<int:pk>/', DeleteQuestion.as_view(), name="delete_question"),
    path('question/get/<int:pk>/', GetQuestion.as_view(), name="get_question"),

    # Answer
    path('answer/create/', CreateAnswer.as_view(), name="create_answer"),
    path('answer/update/<int:pk>/', UpdateAnswer.as_view(), name="update_answer"),
    path('answer/list/', ListAnswer.as_view(), name="list_answer"),
    path('answer/delete/<int:pk>/', DeleteAnswer.as_view(), name="delete_answer"),
    path('answer/get/<int:pk>/', GetAnswer.as_view(), name="get_answer"),

]
