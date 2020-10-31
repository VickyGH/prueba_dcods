from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .permission import IsSuperUser
from .serializers import *


# Course
class CreateCourse(generics.CreateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CourseSerializer


class UpdateCourse(generics.UpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')


class DeleteCourse(generics.DestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')


class ListCourse(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseSerializer
    queryset = Course.objects.all().order_by('id')


class GetCourse(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseSerializer
    queryset = Course.objects.all()

# Lesson
class CreateLesson(generics.CreateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = LessonSerializer


class UpdateLesson(generics.UpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('id')


class DeleteLesson(generics.DestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('id')


class ListLesson(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLessonSerializer
    queryset = Lesson.objects.all().order_by('id')


class GetLesson(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLessonQuestionSerializer
    queryset = Lesson.objects.all()


# Question
class CreateQuestion(generics.CreateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = QuestionSerializer


class UpdateQuestion(generics.UpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all().order_by('id')


class DeleteQuestion(generics.DestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all().order_by('id')


class ListQuestion(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListQuestionSerializer
    queryset = Question.objects.all().order_by('id')


class GetQuestion(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListQuestionSerializer
    queryset = Question.objects.all()


# Answer
class CreateAnswer(generics.CreateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = AnswerSerializer


class UpdateAnswer(generics.UpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all().order_by('id')


class DeleteAnswer(generics.DestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all().order_by('id')


class ListAnswer(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAnswerSerializer
    queryset = Answer.objects.all().order_by('id')


class GetAnswer(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAnswerSerializer
    queryset = Answer.objects.all()


