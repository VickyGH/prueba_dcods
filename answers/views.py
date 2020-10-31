import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .filters import UserFilter
from .models import *
from .serializers import *
from courses.models import Answer as C_Answer, Question as C_Question


# Course x User
class CreateCourse(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseUserSerializer


class UpdateCourse(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseUserSerializer
    queryset = Course.objects.all().order_by('id')


class DeleteCourse(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseUserSerializer
    queryset = Course.objects.all().order_by('id')


class ListCourse(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseUserSerializer
    queryset = Course.objects.all().order_by('id')


class GetCourse(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseUserSerializer
    queryset = Course.objects.all()


# Lesson x User
class CreateLesson(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonUserSerializer


class UpdateLesson(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonUserSerializer
    queryset = Lesson.objects.all().order_by('id')


class DeleteLesson(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonUserSerializer
    queryset = Lesson.objects.all().order_by('id')


class ListLesson(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLessonUserSerializer
    queryset = Lesson.objects.all().order_by('id')


class GetLesson(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLessonUserSerializer
    queryset = Lesson.objects.all()


# Answer
class CreateAnswer(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerUserSerializer


class UpdateAnswer(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerUserSerializer
    queryset = Answer.objects.all().order_by('id')


class DeleteAnswer(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnswerUserSerializer
    queryset = Answer.objects.all().order_by('id')


class ListAnswer(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAnswerUserSerializer
    queryset = Answer.objects.all().order_by('id')


class GetAnswer(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAnswerUserSerializer
    queryset = Answer.objects.all()


#List User
class ListCourseUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCourseUserSerializer
    queryset = Course.objects.all().order_by('id')
    filter_backends = [UserFilter, ]


class ListLessonCourseUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLessonUserSerializer
    queryset = Lesson.objects.all().order_by('id')
    filter_backends = [UserFilter, ]


# Response x User
class AnswersUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ListAnswerUserSerializer
    queryset = Answer.objects.all().order_by('id')
    pagination_class = None

    def create(self, request, *args, **kwargs):
        data = self.request.data
        user = User.objects.get(id=self.request.user.id)
        response = []

        for dt in data:
            question_id = dt['question_id']
            answer_id = dt['answer_id']

            try:
                question = C_Question.objects.get(id=question_id)
                answer = C_Answer.objects.get(id=answer_id, question_id=question.id)
            except:
                question = None
                answer = None

            if question == None or answer == None:
                status = False
            else:
                status = True
                answer_user = Answer.objects.filter(user_id=user.id, question_id=question.id)#, answer_id=answer.id)
                if answer_user.count() == 0 :
                    Answer.objects.create(
                        user_id = user.id,
                        question_id = question.id,
                        answer_id = answer.id,
                        point = answer.point
                    )
                else:
                    Answer.objects.filter(
                        user_id = user.id,
                        question_id = question.id
                    ).update(
                        answer_id=answer.id,
                        point=answer.point
                    )

            response.append({
                "question_id": question_id,
                "answer_id": answer_id,
                "status": status
            })

        # -- possible task with celery
        load_points(user)
        return Response(response, status=200)


def load_points(user):
    courses = Course.objects.filter(user_id=user.id).order_by('id')
    for course in courses:
        lessons = C_Lesson.objects.filter(course_id=course.id)
        for lesson in lessons:
            questions = C_Question.objects.filter(lesson = lesson.id).values_list('id', flat=True)
            answer = Answer.objects.filter(user_id=user.id, question__in=questions).values_list('point', flat=True)
            t1 = sum(answer)
            lesson_user = Lesson.objects.filter(user_id=user.id, lesson_id=lesson.id)#.update()
            if lesson_user.count() == 0:
                Lesson.objects.create(
                    user_id = user.id,
                    lesson_id = lesson.id,
                    status = False,
                    point = t1
                )
            else:
                Lesson.objects.filter(user_id=user.id, lesson_id = lesson.id).update(point = t1)
