from django.contrib.auth.models import User
from django.db import models
from core.helpers.model import TimeStamp
from courses.models import Course as C_Course, Lesson as C_Lesson, Question as C_Question, Answer as C_Answer


class Course(TimeStamp):
    user = models.ForeignKey(User, related_name='user_course_user', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(C_Course, related_name='course_course_user', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    point = models.IntegerField(default=0)


class Lesson(TimeStamp):
    user = models.ForeignKey(User, related_name='user_lesson_user', on_delete=models.SET_NULL, null=True)
    lesson = models.ForeignKey(C_Lesson, related_name='lesson_lesson_user', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    point = models.IntegerField(default=0)


class Answer(TimeStamp):
    user = models.ForeignKey(User, related_name='user_answer_user', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(C_Question, related_name='question_answer_user', on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(C_Answer, related_name='answer_answer_user', on_delete=models.SET_NULL, null=True)
    point = models.IntegerField(default=0)
