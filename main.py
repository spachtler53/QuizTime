# Hauptprogramm – PCEP Quiz Engine "pep_quiz_bakowsky"
# Einstiegspunkt mit interaktivem Menue und allen Bonus-Features

from questions import questions
import quiz_engine
import stats
import random


def show_menu() -> None:
    """Gibt das Hauptmenue auf der Konsole aus."""
    print(f"\n{'═' * 50}")
    print(f"  QUIZ BAKOWSKY")
    print(f"{'═' * 50}")
    print("1.  Quiz starten            (alle Fragen, zufaellig)")
    print("2.  Quiz nach Schwierigkeit (Level 1 / 2 / 3)")
    print("3.  Quiz nach Kategorie     (eine Kategorie waehlen)")
    print("4.  Statistiken anzeigen")
    print("5.  Highscore anzeigen")
    print("6.  Beenden")
    print(f"{'═' * 50}")


def choose_difficulty() -> int:
    """Laesst den Nutzer einen Schwierigkeitsgrad auswaehlen (1-3)."""
    print(f"\n{'─' * 50}")
    print("  Schwierigkeitsstufe waehlen:")
    print("1  ─  Leicht  (nur Level 1 Fragen)")
    print("  2  ─  Mittel  (Level 1 + 2 Fragen)")
    print("  3  ─  Schwer  (alle Fragen, inkl. Level 3)")
    print(f"{'─' * 50}")

    while True:
        try:
            choice: int = int(input("\n  Wahl (1-3): ").strip())
            if 1 <= choice <= 3:
                return choice
            else:
                print("  ⚠  Bitte 1, 2 oder 3 eingeben!")
        except ValueError:
            print("  ⚠  Ungueltige Eingabe – bitte eine Zahl eingeben!")


def choose_category(all_questions: list[dict]) -> str:
    """Laesst den Nutzer eine Kategorie auswaehlen und gibt deren Namen zurueck."""
    categories: list[str] = quiz_engine.get_categories(all_questions)

    print(f"\n{'─' * 50}")
    print("Verfuegbare Kategorien:")
    print(f"{'─' * 50}")

    for i, cat in enumerate(categories, 1):
        count: int = 0
        for q in all_questions:
            if q.get('category') == cat:
                count += 1
        print(f"  {i}.  {cat}  ({count} Fragen)")

    print(f"{'─' * 50}")

    while True:
        try:
            choice: int = int(input(f"\n  Wahl (1-{len(categories)}): ").strip())
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print(f"  ⚠  Bitte eine Zahl zwischen 1 und {len(categories)} eingeben!")
        except ValueError:
            print("  ⚠  Ungueltige Eingabe – bitte eine Zahl eingeben!")


def start_quiz(quiz_questions: list[dict], all_results: list[dict]) -> None:
    """Mischt die Fragen, startet das Quiz und speichert das Ergebnis."""
    if not quiz_questions:
        print("\n  ⚠  Keine Fragen fuer diese Auswahl gefunden!")
        return

    shuffled: list[dict] = quiz_questions.copy()
    random.shuffle(shuffled)

    print(f"\n  Quiz startet mit {len(shuffled)} Frage(n)...")
    input("  Druecke Enter zum Starten...\n")

    result: dict = quiz_engine.run_quiz(shuffled)
    quiz_engine.display_results(result)
    all_results.append(result)

    if result['wrong'] > 0:
        review: str = input("  Falsche Antworten anzeigen? (j/n): ").strip().lower()
        if review == "j":
            quiz_engine.display_wrong_answers(result)


def main() -> None:
    """Hauptprogramm: initialisiert den Ergebnis-Speicher und startet die Menue-Schleife."""
    all_results: list[dict] = []

    print(f"\n{'═' * 50}")
    print("  Willkommen bei der PCEP Quiz Engine!")
    print("  Projekt: pep_quiz_bakowsky")
    print(f"  {len(questions)} Fragen in 5 Kategorien bereit.")
    print(f"{'═' * 50}")

    while True:
        show_menu()

        try:
            choice: str = input("\n  Deine Wahl (1-6): ").strip()

            if choice == "1":
                # Alle Fragen, zufaellig gemischt
                start_quiz(questions, all_results)

            elif choice == "2":
                # Nach Schwierigkeitsgrad filtern
                difficulty: int = choose_difficulty()
                filtered: list[dict] = quiz_engine.filter_by_difficulty(questions, difficulty)
                label: str = ["", "Leicht", "Mittel", "Schwer"][difficulty]
                print(f"\n  {len(filtered)} Fragen fuer Schwierigkeit '{label}' gefunden.")
                start_quiz(filtered, all_results)

            elif choice == "3":
                # Nach Kategorie filtern
                category: str = choose_category(questions)
                filtered = quiz_engine.filter_by_category(questions, category)
                print(f"\n  {len(filtered)} Fragen in der Kategorie '{category}' gefunden.")
                start_quiz(filtered, all_results)

            elif choice == "4":
                # Vollstaendige Statistiken anzeigen
                stats.display_full_stats(all_results)

            elif choice == "5":
                # Highscore anzeigen
                if all_results:
                    hs: dict = stats.get_highscore(all_results)
                    print(f"\n  ★  HIGHSCORE: {hs['correct']}/{hs['total']} ({hs['percentage']:.1f}%)")
                else:
                    print("\n  Noch kein Highscore – spiel zuerst ein Quiz!")

            elif choice == "6":
                # Programm beenden
                print("\n  Auf Wiedersehen! Viel Erfolg bei der PCEP-Pruefung!")
                break

            else:
                print("  ⚠  Ungueltige Auswahl – bitte 1 bis 6 eingeben.")

        except KeyboardInterrupt:
            print("\n\n  Quiz unterbrochen. Auf Wiedersehen!")
            break
        except Exception as e:
            print(f"  ⚠  Unerwarteter Fehler: {e}")


if __name__ == '__main__':
    main()
