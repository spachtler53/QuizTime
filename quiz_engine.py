from typing import Optional


def display_question(question: dict, num: int, total: int) -> None:
    """Zeigt eine Frage mit Nummer, Kategorie, Schwierigkeit und Antwortoptionen an."""
    difficulty: int = question.get('difficulty', 1)
    stars: str = "★" * difficulty + "☆" * (3 - difficulty)
    category: str = question.get('category', 'Unbekannt')

    # Einzeiligen Frage-Text mit Einrueckung formatieren
    question_text: str = question['question'].replace('\n', '\n  ')

    print(f"\n{'─' * 58}")
    print(f"  Frage {num}/{total}   |   {category}   |   {stars}")
    print(f"{'─' * 58}")
    print(f"\n  {question_text}\n")

    for i, option in enumerate(question['options'], 1):
        print(f"  {i}.  {option}")
    print()


def get_answer(question: dict) -> int:
    """Liest und validiert die Antwort des Nutzers (nur gueltige Zahlen im Bereich)."""
    num_options: int = len(question['options'])

    while True:
        try:
            raw: str = input(f"  Deine Antwort (1-{num_options}): ").strip()
            answer: int = int(raw)
            if 1 <= answer <= num_options:
                return answer
            else:
                print(f"  ⚠  Bitte eine Zahl zwischen 1 und {num_options} eingeben!")
        except ValueError:
            print("  ⚠  Ungueltige Eingabe – bitte eine Zahl eingeben!")


def check_answer(answer: int, question: dict) -> bool:
    """Prueft, ob die gegebene Antwort (1-basiert) korrekt ist."""
    return (answer - 1) == question['correct_index']


def _display_question_result(is_correct: bool, question: dict) -> None:
    """Gibt nach einer Frage aus, ob die Antwort stimmt und zeigt die Erklaerung."""
    if is_correct:
        print("  ✓  Richtig! Gut gemacht!")
    else:
        correct_option: str = question['options'][question['correct_index']]
        print(f"  ✗  Falsch!  Richtige Antwort: {correct_option}")

    explanation: str = question['explanation'].replace('\n', '\n  ')
    print(f"  »  {explanation}")


def _display_progress(correct: int, total_answered: int) -> None:
    """Zeigt einen Echtzeit-Fortschrittsbalken nach jeder beantworteten Frage."""
    if total_answered == 0:
        return

    percentage: float = (correct / total_answered) * 100
    bar_length: int = 24
    filled: int = int(bar_length * correct / total_answered)
    bar: str = "█" * filled + "░" * (bar_length - filled)

    print(f"\n  Fortschritt: [{bar}] {correct}/{total_answered} ({percentage:.0f}%)\n")


def run_quiz(questions: list[dict]) -> dict:
    """Fuehrt ein komplettes Quiz durch und gibt ein Ergebnis-Dictionary zurueck."""
    results: dict = {
        'total': len(questions),
        'correct': 0,
        'wrong': 0,
        'details': []
    }

    for i, question in enumerate(questions, 1):
        display_question(question, i, len(questions))
        answer: int = get_answer(question)
        is_correct: bool = check_answer(answer, question)

        if is_correct:
            results['correct'] += 1
        else:
            results['wrong'] += 1

        _display_question_result(is_correct, question)
        _display_progress(results['correct'], i)

        results['details'].append({
            'question': question['question'],
            'correct': is_correct,
            'category': question.get('category', 'Unbekannt'),
            'difficulty': question.get('difficulty', 1)
        })

    return results


def display_results(results: dict) -> None:
    """Zeigt die abschliessenden Gesamtergebnisse eines Quiz an."""
    if results['total'] == 0:
        print("  Keine Fragen im Quiz!")
        return

    percentage: float = (results['correct'] / results['total']) * 100

    if percentage >= 80:
        grade: str = "★★★  Ausgezeichnet!"
    elif percentage >= 60:
        grade = "★★☆  Gut gemacht!"
    elif percentage >= 40:
        grade = "★☆☆  Weiter ueben!"
    else:
        grade = "☆☆☆  Mehr lernen!"

    print(f"\n{'═' * 58}")
    print(f"  QUIZ BEENDET  ─  {grade}")
    print(f"{'═' * 58}")
    print(f"  Korrekt:  {results['correct']}/{results['total']} ({percentage:.1f}%)")
    print(f"  Falsch:   {results['wrong']}/{results['total']}")
    print(f"{'─' * 58}")

    # Auswertung nach Kategorie
    category_stats: dict = {}
    for detail in results['details']:
        cat: str = detail['category']
        if cat not in category_stats:
            category_stats[cat] = {'correct': 0, 'total': 0}
        category_stats[cat]['total'] += 1
        if detail['correct']:
            category_stats[cat]['correct'] += 1

    if category_stats:
        print("\n  Ergebnisse nach Kategorie:")
        for cat, s in category_stats.items():
            cat_pct: float = (s['correct'] / s['total']) * 100
            icon: str = "✓" if cat_pct >= 60 else "✗"
            print(f"  {icon}  {cat}: {s['correct']}/{s['total']} ({cat_pct:.0f}%)")

    print(f"{'═' * 58}\n")


# ─── Bonus-Hilfsfunktionen ────────────────────────────────────────────────────

def filter_by_difficulty(questions: list[dict], max_difficulty: int) -> list[dict]:
    """Gibt alle Fragen zurueck, deren Schwierigkeit <= max_difficulty ist."""
    filtered: list[dict] = []
    for q in questions:
        if q.get('difficulty', 1) <= max_difficulty:
            filtered.append(q)
    return filtered


def filter_by_category(questions: list[dict], category: str) -> list[dict]:
    """Gibt alle Fragen einer bestimmten Kategorie zurueck."""
    filtered: list[dict] = []
    for q in questions:
        if q.get('category', '') == category:
            filtered.append(q)
    return filtered


def get_categories(questions: list[dict]) -> list[str]:
    """Gibt eine Liste aller einzigartigen Kategorien aus der Fragen-Datenbank zurueck."""
    categories: list[str] = []
    for q in questions:
        cat: str = q.get('category', 'Unbekannt')
        if cat not in categories:
            categories.append(cat)
    return categories


def display_wrong_answers(results: dict) -> None:
    """Zeigt nach dem Quiz alle falsch beantworteten Fragen zur Wiederholung an."""
    wrong: list[dict] = []
    for detail in results['details']:
        if not detail['correct']:
            wrong.append(detail)

    if not wrong:
        print("\n  Alle Antworten waren korrekt – nichts zu wiederholen!")
        return

    print(f"\n{'─' * 58}")
    print(f"  FALSCHE ANTWORTEN ({len(wrong)} Stueck) – zur Wiederholung:")
    print(f"{'─' * 58}")

    for i, detail in enumerate(wrong, 1):
        # Frage-Text aus results kuerzen fuer Uebersicht
        question_preview: str = detail['question']
        if len(question_preview) > 50:
            question_preview = question_preview[:47] + "..."
        question_preview = question_preview.replace('\n', ' ')
        print(f"  {i}.  [{detail['category']}]  {question_preview}")

    print(f"{'─' * 58}\n")
