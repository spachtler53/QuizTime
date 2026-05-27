from questions import questions

placeholder = 50 * "\033[96m_\033[94m"


def show_menu() -> None:
    print(placeholder)
    print("\t\t\tWillkommen bei QuizTimes!")
    print(placeholder)

    print("\033[3m\033[91mBitte wähle im Menü aus:\n\033[0m")

    print(
        "\033[93m> 1. Schnelles Quiz starten\033[0m\n"
        "\033[93m> 2. Themenbereich auswählen\033[0m\n"
        "\033[93m> 3. Statistiken ansehen\033[0m"
    )

    print(placeholder)


def quiz_starten(questions):
    score = 0

    for i, q in enumerate(questions):
        print(f"\nFrage {i + 1}: {q['question']}")

        for idx, option in enumerate(q["options"]):
            print(f"{idx + 1}. {option}")

        answer = input("Deine Antwort (1-4): ")

        if answer.isdigit():
            answer_index = int(answer) - 1

            if answer_index == q["correct_index"]:
                print("\033[92mRichtig!\033[0m")
                score += 1
            else:
                print("\033[91mFalsch!\033[0m")
                print(f"Erklärung: {q['explanation']}")
        else:
            print("Bitte nur Zahlen eingeben.")

    print(f"\nDu hast {score}/{len(questions)} richtig.")


show_menu()
quiz_starten(questions)