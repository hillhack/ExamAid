# exams/urls.py
from django.urls import path
from .views import ExamAPIView, SubmitAnswersView, take_exam_view

urlpatterns = [
    path('take/', take_exam_view, name='take_exam'),  # HTML page
    # Fetch questions from API or local DB
    path('api/', ExamAPIView.as_view(), name='exam-api'),

    # Submit answers and calculate score
    path('submit/', SubmitAnswersView.as_view(), name='submit-answers'),
]
