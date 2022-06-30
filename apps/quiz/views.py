from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Quiz_Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class QuizQuestion(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        quiz = Quiz_Question.objects.filter(quiz=kwargs['pk'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


class SingleQuestion(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        qs = Quiz_Question.objects.filter(quiz=kwargs['topic'])
        question = qs.filter(id=kwargs['pk'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
