from pathlib import Path
placeholder = 50 * "\033[96m_\033[94m"
questions_file = Path("questions.py")
def show_menu() -> None:
    print(placeholder)
    print("\t\t\t"
          "Willkommen bei QuizTimes!")
    print(placeholder)
    print("\033[3m\033[91mBitte Wähle im Menü aus:\n\033[0m")
    print("\033[93m> 1. Schnelles Quiz starten\033[90m\n"
          "\033[93m> 2. Themenbereich auswählen\033[90m\n"
          "\033[93m> 3. Statistiken ansehen\033[90m")
    print(placeholder)


def quiz_starten(questions: questions_file):
      score = 0

      for i in range (len(questions)):
          print(f"\nFrage {i + 1}: {questions[i]['question']}")
          for idx, option in enumerate(questions[i]['options']):
              print(f"{idx + 1}. {option}")
          answer = input("Deine Antwort (1-4): ")
          if answer.isdigit() and int(answer) == questions[i]['answer']:
              print("\033[92mRichtig!\033[0m")
              score += 1
          else:
              print("\033[91mFalsch!\033[0m")

quiz_starten(questions_file)