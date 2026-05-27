# Statistik-Modul – Verarbeitung und Anzeige aller Quiz-Ergebnisse
# Enthaelt: Gesamtstatistik, Kategorienauswertung, Best/Worst Category, Highscore

def calculate_category_stats(all_results: list[dict]) -> dict:
    """Berechnet kumulierte Statistiken pro Kategorie ueber alle gespielten Quizze."""
    category_stats: dict = {}

    for result in all_results:
        for detail in result['details']:
            cat: str = detail['category']
            if cat not in category_stats:
                category_stats[cat] = {'correct': 0, 'total': 0}
            category_stats[cat]['total'] += 1
            if detail['correct']:
                category_stats[cat]['correct'] += 1

    return category_stats


def get_best_category(category_stats: dict) -> str:
    """Gibt den Namen der Kategorie mit der hoechsten Trefferquote zurueck."""
    if not category_stats:
        return "Keine Daten"

    best_cat: str = ""
    best_pct: float = -1.0

    for cat, s in category_stats.items():
        if s['total'] > 0:
            pct: float = s['correct'] / s['total']
            if pct > best_pct:
                best_pct = pct
                best_cat = cat

    return best_cat


def get_worst_category(category_stats: dict) -> str:
    """Gibt den Namen der Kategorie mit der niedrigsten Trefferquote zurueck."""
    if not category_stats:
        return "Keine Daten"

    worst_cat: str = ""
    worst_pct: float = 2.0  # Startwert hoeher als 100%

    for cat, s in category_stats.items():
        if s['total'] > 0:
            pct: float = s['correct'] / s['total']
            if pct < worst_pct:
                worst_pct = pct
                worst_cat = cat

    return worst_cat


def get_highscore(all_results: list[dict]) -> dict:
    """Gibt den besten erzielten Score (als Dictionary) aus allen Quizzen zurueck."""
    if not all_results:
        return {'correct': 0, 'total': 0, 'percentage': 0.0}

    best: dict = all_results[0]
    best_pct: float = best['correct'] / best['total'] if best['total'] > 0 else 0.0

    for i in range(1, len(all_results)):
        result: dict = all_results[i]
        if result['total'] > 0:
            pct: float = result['correct'] / result['total']
            if pct > best_pct:
                best_pct = pct
                best = result

    return {
        'correct': best['correct'],
        'total': best['total'],
        'percentage': best_pct * 100
    }


def display_full_stats(all_results: list[dict]) -> None:
    """Zeigt eine vollstaendige Uebersicht aller bisherigen Quiz-Ergebnisse an."""
    if not all_results:
        print("\n  Noch keine Quiz-Ergebnisse vorhanden – spiel zuerst ein Quiz!")
        return

    total_quizzes: int = len(all_results)
    total_questions: int = 0
    total_correct: int = 0

    for result in all_results:
        total_questions += result['total']
        total_correct += result['correct']

    overall_pct: float = (total_correct / total_questions * 100) if total_questions > 0 else 0.0

    category_stats: dict = calculate_category_stats(all_results)
    best_cat: str = get_best_category(category_stats)
    worst_cat: str = get_worst_category(category_stats)
    highscore: dict = get_highscore(all_results)

    print(f"\n{'═' * 58}")
    print(f"  DEINE STATISTIKEN")
    print(f"{'═' * 58}")
    print(f"  Gespielte Quizze:       {total_quizzes}")
    print(f"  Fragen gesamt:          {total_questions}")
    print(f"  Richtig gesamt:         {total_correct} ({overall_pct:.1f}%)")
    print(f"  Highscore:              {highscore['correct']}/{highscore['total']} ({highscore['percentage']:.1f}%)")
    print(f"{'─' * 58}")
    print(f"  ★  Beste Kategorie:      {best_cat}")
    print(f"  ✗  Schwaechste Kategorie: {worst_cat}")
    print(f"{'─' * 58}")

    # Detaillierter Quiz-Verlauf
    print("\n  Quiz-Verlauf:")
    for i, result in enumerate(all_results, 1):
        if result['total'] > 0:
            pct: float = (result['correct'] / result['total']) * 100
            bar_length: int = 12
            filled: int = int(bar_length * result['correct'] / result['total'])
            bar: str = "█" * filled + "░" * (bar_length - filled)
            print(f"  Quiz {i}: [{bar}] {result['correct']}/{result['total']} ({pct:.0f}%)")

    # Kategorie-Uebersicht
    if category_stats:
        print(f"\n  Kategorien-Uebersicht:")
        for cat, s in category_stats.items():
            cat_pct: float = (s['correct'] / s['total'] * 100) if s['total'] > 0 else 0.0
            icon: str = "✓" if cat_pct >= 60 else "✗"
            bar_length = 10
            filled = int(bar_length * s['correct'] / s['total']) if s['total'] > 0 else 0
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"  {icon}  {cat:<22} [{bar}] {s['correct']}/{s['total']} ({cat_pct:.0f}%)")

    print(f"{'═' * 58}\n")
