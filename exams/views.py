# exams/views.py
import random
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import fetch_questions_from_opentdb
from .models import QuestionBank, Attempt

# -------------------------
# HTML view for exam page
# -------------------------
def take_exam_view(request):
    category_id = int(request.GET.get('category_id', 17))  # Open Trivia DB category
    num_questions = int(request.GET.get('num', 10))
    category_name = request.GET.get('category_name', None)  # optional local category

    questions = []

    # Try external API first
    try:
        questions = fetch_questions_from_opentdb(category_id, num_questions)
    except Exception:
        questions = []

    # Fallback to local DB if API fails
    if not questions and category_name:
        local_questions = list(QuestionBank.objects.filter(category=category_name))
        if local_questions:
            selected_questions = random.sample(
                local_questions, 
                min(len(local_questions), num_questions)
            )
            for q in selected_questions:
                questions.append({
                    "id": q.id,
                    "question_text": q.question_text,
                    "option1": q.option1,
                    "option2": q.option2,
                    "option3": q.option3,
                    "option4": q.option4,
                    "correct_option": q.correct_option
                })

    # Remove correct options if you want to hide them in template
    for q in questions:
        q.pop("correct_option", None)

    return render(request, "exam.html", {"questions": questions})

# -------------------------
# JSON API view (existing)
# -------------------------
class ExamAPIView(APIView):
    """
    Fetch questions for a given category.
    Returns JSON (for API use)
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        category_id = int(request.GET.get('category_id', 17))
        num_questions = int(request.GET.get('num', 10))
        category_name = request.GET.get('category_name', None)

        questions = []

        try:
            questions = fetch_questions_from_opentdb(category_id, num_questions)
        except Exception:
            questions = []

        if not questions and category_name:
            local_questions = list(QuestionBank.objects.filter(category=category_name))
            if local_questions:
                selected_questions = random.sample(
                    local_questions,
                    min(len(local_questions), num_questions)
                )
                for q in selected_questions:
                    questions.append({
                        "id": q.id,
                        "question_text": q.question_text,
                        "option1": q.option1,
                        "option2": q.option2,
                        "option3": q.option3,
                        "option4": q.option4,
                        "correct_option": q.correct_option
                    })

        if not questions:
            return Response({"error": "No questions available."}, status=404)

        for q in questions:
            q.pop("correct_option", None)

        return Response({"questions": questions})

# -------------------------
# Submit answers API view
# -------------------------
class SubmitAnswersView(APIView):
    """
    Submit answers and calculate score
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        answers = request.data.get("answers")  # {question_id: selected_option}
        if not answers:
            return Response({"error": "No answers provided."}, status=status.HTTP_400_BAD_REQUEST)

        score = 0
        for q_id, answer in answers.items():
            try:
                question = get_object_or_404(QuestionBank, id=q_id)
                if int(answer) == question.correct_option:
                    score += 1
            except:
                continue

        Attempt.objects.create(student=request.user, score=score, completed=True)

        return Response({"score": score, "total": len(answers)})
