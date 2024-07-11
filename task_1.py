import random

def quiz():
    questions = [
        {
            "question": "Which team won the last T20 World Cup?",
            "options": ["A.India", "B.Australia", "C.South Africa", "D.England"],
            "answer": "A"
        },
        {
            "question": "What is the capital of India?",
            "options": ["A.Gandhinagar", "B.Mumbai", "C.Delhi", "D.Ahmedabad"],
            "answer": "C"
        },
        {
            "question": "What is 2+2?",
            "options": ["A.4", "B.1", "C.3", "D.6"],
            "answer": "A"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A.Elephant", "B.Blue whale", "C.Giraffe", "D.Orca"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A.Earth", "B.Mars", "C.Jupiter", "D.Saturn"],
            "answer": "B"
        }
    ]

    random.shuffle(questions)
    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Your answer is (A, B, C, D): ").upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")

    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz()
