# ExamAid

A modern web-based examination platform designed to make online assessments **seamless, secure, and intelligent**.

---

## ✨ Key Features

* **User-Friendly Interface** → Responsive design for students and administrators.
* **Secure Authentication** → Role-based login for students and admins.
* **Smart Exam Engine** → Timed exams, autosave, and proctoring support.
* **Auto-Evaluation** → Automatic grading for MCQs and AI-assisted evaluation for descriptive answers.
* **Analytics Dashboard** → Track performance, generate reports, and view insights.
* **Admin Controls** → Add/manage exams, questions, and user roles easily.

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/hillhack/ExamAid.git
cd ExamAid
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .examenv
source .examenv/bin/activate   # Linux/macOS
# .examenv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is not available, install Django manually: `pip install django djangorestframework`)*

### 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/admin/` to access the admin panel.

---

## ⚙️ API Endpoints (Examples)

* **Register User** → `POST /api/register/`
* **Login User** → `POST /api/login/`
* **Generate Exam** → `GET /api/generate_exam/?category=NEET&num=10`
* **Submit Answers** → `POST /api/submit_answers/`

All endpoints require **authentication** except user registration.

---

## 📦 Project Structure

```
ExamAid/
├── accounts/           # Custom user model, serializers, views
├── exams/              # Exam, QuestionBank, Attempt models
├── ExamAid/            # Project settings
├── manage.py
├── requirements.txt
└── README.md
```

