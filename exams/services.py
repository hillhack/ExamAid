# exams/services.py
import requests

def fetch_questions_from_opentdb(category_id=17, num_questions=10):
    url = f"https://opentdb.com/api.php?amount={num_questions}&category={category_id}&type=multiple"
    response = requests.get(url)
    data = response.json()

    questions = []
    for item in data['results']:
        questions.append({
            "question_text": item['question'],
            "option1": item['incorrect_answers'][0],
            "option2": item['incorrect_answers'][1],
            "option3": item['incorrect_answers'][2],
            "option4": item['correct_answer'],
            "correct_option": 4
        })
    return questions
