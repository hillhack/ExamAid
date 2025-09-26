# ExamAid
A modern web-based examination platform designed to make online assessments seamless, secure, and intelligent.
✨ Key Highlights

    User-Friendly Interface → Simple and responsive design for students and administrators.

    Secure Authentication → Role-based login for students and admins.

    Smart Exam Engine → Timed exams, autosave, and proctoring features.

    Auto-Evaluation → Automatic grading for MCQs and AI-powered evaluation for descriptive answers.

    Analytics Dashboard → Performance insights and result tracking.

    Admin Controls → Add/manage exams, questions, and user roles.
Install it¶

Next, run the Django command-line utilities to create the database tables automatically:
/ 
python3 -m venv .examenv
source .examenv/bin/activate
pip install django
cd ExamAid
python manage.py migrate

