from rest_framework import serializers
from courses.models import *

# Course
class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class ListCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


# Lesson
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ListLessonSerializer(serializers.ModelSerializer):
    course = ListCourseSerializer(many=False)
    class Meta:
        model = Lesson
        fields = '__all__'


# Answer
class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class ListAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'

# Question
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class ListQuestionSerializer(serializers.ModelSerializer):
    lesson = ListLessonSerializer(many=False)
    question_answer = ListAnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'

#
class ListQuestionAnswerSerializer(serializers.ModelSerializer):
    #lesson = ListLessonSerializer(many=False)
    question_answer = ListAnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'


class ListLessonQuestionSerializer(serializers.ModelSerializer):
    course = ListCourseSerializer(many=False)
    lesson_question = ListQuestionAnswerSerializer(many=True)
    class Meta:
        model = Lesson
        fields = '__all__'

