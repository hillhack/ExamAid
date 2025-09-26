# exams/models.py
from django.db import models
from django.conf import settings

# Categories for exams
CATEGORY_CHOICES = [
    ("NEET", "NEET"),
    ("JEE", "JEE"),
    # Add more categories later
]

# Question Bank Model
class QuestionBank(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    question_text = models.TextField()
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    correct_option = models.PositiveSmallIntegerField()  # 1, 2, 3, 4
    source = models.CharField(max_length=100, blank=True, null=True)  # optional, track source of question

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category}: {self.question_text[:50]}"

# Student Attempt Model
class Attempt(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    total_questions = models.PositiveSmallIntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - Score: {self.score}/{self.total_questions}"

# Exam Session Model
class Exam(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    questions = models.ManyToManyField(QuestionBank)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    score = models.PositiveSmallIntegerField(default=0)
    is_completed = models.BooleanField(default=False)  # track exam completion

    class Meta:
        ordering = ['-started_at']

    def __str__(self):
        return f"{self.student.username} - {self.category} Exam"
