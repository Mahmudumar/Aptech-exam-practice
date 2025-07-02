import os
from bs4 import BeautifulSoup

def extract_questions_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    all_rows = soup.find_all("tr")
    questions = []
    current_question = ""
    options = []
    correct_option_index = -1

    for row in all_rows:
        text = row.get_text(strip=True)

        # Detect question
        if text and text[0].isdigit() and '.' in text:
            if current_question:
                questions.append({
                    "question": current_question,
                    "options": options,
                    "answer": correct_option_index + 1
                })
                options = []
                correct_option_index = -1

            current_question = text.split("(")[0].strip()

        # Detect options
        lis = row.find_all("li")
        for li in lis:
            option_text = li.get_text(strip=True)
            options.append(option_text)
            if 'color:red' in li.attrs.get('style', ''):
                correct_option_index = len(options) - 1

    # Add last question
    if current_question and options:
        questions.append({
            "question": current_question,
            "options": options,
            "answer": correct_option_index + 1
        })

    return questions

def start_quiz(questions):
    score = 0
    print("\n🎓 Welcome to the CLI Exam Practice!")
    print("📋 There are", len(questions), "questions. Good luck!\n")

    for q in questions:
        print(q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"  {i}. {opt}")
        try:
            ans = int(input("Your answer (1-4): "))
            if ans == q["answer"]:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer was: {q['options'][q['answer'] - 1]}\n")
        except:
            print("⚠️ Invalid input. Moving on...\n")

    print(f"🏁 Your Final Score: {score}/{len(questions)}")
    print("📚 Review your wrong answers to improve!")

def main():
    print("=== Aptech Exam .HTM CLI Runner ===")
    file = input("Enter path to your .htm file (e.g., 1.htm): ").strip()

    if not os.path.exists(file):
        print("⚠️ File not found. Please check the path.")
        return

    questions = extract_questions_from_file(file)
    if not questions:
        print("⚠️ No questions found in the file.")
        return

    start_quiz(questions)

if __name__ == "__main__":
    main()
