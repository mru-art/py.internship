def run_quiz():
    questions = [
        {
            "question": "What is the capital of Hungary?",
            "options": ["a) Budapest", "b) Oslo", "c) Delhi", "d) Madrid"],
            "answer": "a"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Neptune", "b) Mercury", "c) Mars", "d) Earth"],
            "answer": "c"
        },
        {
            "question": "Who wrote 'A Song of Ice and Fire'?",
            "options": ["a) J.K. Rowling", "b) George R.R. Martin", "c) Coleen Hoover", "d) C.S. Lewis"],
            "answer": "b"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["a) Gallium", "b) Titanium", "c) Mercury", "d) Diamond"],
            "answer": "d"
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        user_answer = input("Please enter your answer (e.g., a, b, c, d): ").strip().lower()
        
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.")
        
        print()  # Newline for better readability

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
