from rest_framework import serializers
from .models import Quizzes, Quiz_Question, Quiz_Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'id',
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Quiz_Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Quiz_Question
        fields = [
            'title', 'answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:

        model = Quiz_Question
        fields = [
            'quiz', 'title', 'answer'
        ]
