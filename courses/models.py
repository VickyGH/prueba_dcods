from django.db import models
from core.helpers.model import TimeStamp

Question_Type_Choice = (
    (1, 'Boolean'),
    (2, 'One Answer Correct'),
    (3, 'More One Answer Correct'),
    (4, 'More One Answer Correct'),
)


class Course(TimeStamp):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=True)


class Lesson(TimeStamp):
    course = models.ForeignKey(Course, related_name='course_lesson', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=99)


class Question(TimeStamp):
    lesson = models.ForeignKey(Lesson, related_name='lesson_question', on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=500, blank=True)
    type = models.CharField(max_length=100, blank=True, choices=Question_Type_Choice)


class Answer(TimeStamp):
    question = models.ForeignKey(Question, related_name='question_answer', on_delete=models.SET_NULL, null=True)
    name = models.TextField()
    value = models.TextField()
    correct = models.BooleanField(default=False)
    point = models.IntegerField(default=0)

