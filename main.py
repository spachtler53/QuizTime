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


