def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")

    print("\n--- Quiz Finished ---")
    print(f"Your final score: {score}/{len(questions)}")

# Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"],
        "answer": "B"
    },
    {
        "question": "Which is the largest planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Guido van Rossum", "B. Elon Musk", "C. James Gosling", "D. Dennis Ritchie"],
        "answer": "A"
    }
]

# Run game
run_quiz(questions)
