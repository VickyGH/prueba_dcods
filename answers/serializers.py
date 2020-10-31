from rest_framework import serializers
from accounts.serializers import UserSerializer
from answers.models import *
from courses.serializers import ListCourseSerializer, ListLessonSerializer, ListAnswerSerializer, QuestionSerializer


class CourseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ListCourseUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    course = ListCourseSerializer(many=False)
    class Meta:
        model = Course
        fields = '__all__'


# Lesson
class LessonUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ListLessonUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    lesson = ListLessonSerializer(many=False)
    class Meta:
        model = Lesson
        fields = '__all__'


# Answer
class AnswerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class ListAnswerUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    question = QuestionSerializer(many=False)
    answer = ListAnswerSerializer(many=False)
    class Meta:
        model = Answer
        fields = '__all__'


