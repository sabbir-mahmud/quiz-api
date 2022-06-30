from django.urls import path
from . import views


urlpatterns = [
    path('', views.Quiz.as_view(), name='quiz'),
    path('<str:pk>/', views.QuizQuestion.as_view(), name='questions'),
    path('<str:topic>/<str:pk>', views.SingleQuestion.as_view(), name='questions'),
]
