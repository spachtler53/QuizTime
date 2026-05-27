questions: list[dict] = [
    # ─── Datentypen ──────────────────────────────────────────────────────────────
    {
        'question': "Welcher Datentyp ist `5.0`?",
        'options': ["int", "float", "str", "bool"],
        'correct_index': 1,
        'explanation': "5.0 hat einen Dezimalpunkt, daher ist es ein float.",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was ist der Typ von `True`?",
        'options': ["int", "str", "float", "bool"],
        'correct_index': 3,
        'explanation': "True und False sind Boolean-Werte (bool) in Python.",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was ist der Typ von `[1, 2, 3]`?",
        'options': ["tuple", "dict", "set", "list"],
        'correct_index': 3,
        'explanation': "Eckige Klammern [ ] erstellen eine Liste (list).",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was ergibt `bool([])` in Python?",
        'options': ["True", "Error", "None", "False"],
        'correct_index': 3,
        'explanation': "Eine leere Liste ist 'falsy' in Python: bool([]) = False.",
        'category': "Datentypen",
        'difficulty': 2
    },
    {
        'question': "Was ergibt `type(True) == type(1)`?",
        'options': ["True", "Error", "None", "False"],
        'correct_index': 3,
        'explanation': "type(True) ist bool, type(1) ist int. bool != int, also False.\n  Hinweis: isinstance(True, int) waere True, weil bool eine Unterklasse von int ist!",
        'category': "Datentypen",
        'difficulty': 3
    },

    # ─── Operatoren ──────────────────────────────────────────────────────────────
    {
        'question': "Was gibt `3 // 2` aus?",
        'options': ["1.5", "1", "2", "Error"],
        'correct_index': 1,
        'explanation': "// ist Floor Division (Ganzzahldivision): 3 // 2 = 1.",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Was ergibt `10 % 3`?",
        'options': ["3", "3.33", "0", "1"],
        'correct_index': 3,
        'explanation': "% ist der Modulo-Operator: 10 = 3 * 3 + 1, also Rest 1.",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Was ergibt `2 ** 4`?",
        'options': ["6", "8", "16", "12"],
        'correct_index': 2,
        'explanation': "** ist der Potenz-Operator: 2^4 = 16.",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Was ist der Unterschied zwischen `=` und `==`?",
        'options': [
            "Kein Unterschied",
            "= vergleicht, == weist zu",
            "= weist zu, == vergleicht",
            "Beide vergleichen"
        ],
        'correct_index': 2,
        'explanation': "= ist der Zuweisungsoperator, == ist der Vergleichsoperator.",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Was ergibt `not True`?",
        'options': ["True", "None", "Error", "False"],
        'correct_index': 3,
        'explanation': "not invertiert den Boolean-Wert: not True = False.",
        'category': "Operatoren",
        'difficulty': 1
    },
    {
        'question': "Welches Ergebnis liefert `'Ha' * 3`?",
        'options': ["Error", "Ha Ha Ha", "3Ha", "HaHaHa"],
        'correct_index': 3,
        'explanation': "String-Multiplikation wiederholt den String: 'Ha' * 3 = 'HaHaHa'.",
        'category': "Operatoren",
        'difficulty': 2
    },

    # ─── Kontrollstrukturen ──────────────────────────────────────────────────────
    {
        'question': "Wie viele Male wird gedruckt?\n  for i in range(3):\n      print('x')",
        'options': ["2", "4", "3", "0"],
        'correct_index': 2,
        'explanation': "range(3) erzeugt 0, 1, 2 – also genau 3 Iterationen.",
        'category': "Kontrollstrukturen",
        'difficulty': 1
    },
    {
        'question': "Was gibt folgender Code aus?\n  x = 5\n  if x > 3:\n      print('A')\n  else:\n      print('B')",
        'options': ["B", "AB", "nichts", "A"],
        'correct_index': 3,
        'explanation': "5 > 3 ist True, daher wird der if-Zweig ausgefuehrt: 'A'.",
        'category': "Kontrollstrukturen",
        'difficulty': 1
    },
    {
        'question': "Was bewirkt `break` in einer Schleife?",
        'options': [
            "Aktuelle Iteration ueberspringen",
            "Schleife pausieren",
            "Nichts",
            "Schleife sofort beenden"
        ],
        'correct_index': 3,
        'explanation': "break beendet die gesamte Schleife sofort.",
        'category': "Kontrollstrukturen",
        'difficulty': 1
    },
    {
        'question': "Was macht `continue` in einer Schleife?",
        'options': [
            "Schleife beenden",
            "Zum naechsten Durchlauf springen, Rest ueberspringen",
            "Schleife neu starten",
            "Nichts"
        ],
        'correct_index': 1,
        'explanation': "continue ueberspringt den Rest des aktuellen Durchlaufs und springt zur naechsten Iteration.",
        'category': "Kontrollstrukturen",
        'difficulty': 2
    },
    {
        'question': "Was gibt `range(1, 6, 2)` als Werte aus?",
        'options': ["1, 3, 5", "1, 2, 3, 4, 5", "2, 4, 6", "1, 3, 5, 7"],
        'correct_index': 0,
        'explanation': "range(start=1, stop=6, step=2): Startet bei 1, Schrittweite 2, hoert vor 6 auf → 1, 3, 5.",
        'category': "Kontrollstrukturen",
        'difficulty': 2
    },

    # ─── Syntax ──────────────────────────────────────────────────────────────────
    {
        'question': "Wie lautet die korrekte Syntax fuer einen einzeiligen Kommentar?",
        'options': ["// Kommentar", "-- Kommentar", "# Kommentar", "/* Kommentar */"],
        'correct_index': 2,
        'explanation': "In Python beginnen einzeilige Kommentare mit dem # Zeichen.",
        'category': "Syntax",
        'difficulty': 1
    },
    {
        'question': "Was gibt `len('Python')` zurueck?",
        'options': ["5", "7", "Error", "6"],
        'correct_index': 3,
        'explanation': "Der String 'Python' hat genau 6 Zeichen.",
        'category': "Syntax",
        'difficulty': 1
    },
    {
        'question': "Welcher Ausdruck ist ein gueltiger f-String?",
        'options': ['f("text {var}")', '"text {var}"', 'format("text")', 'f"text {var}"'],
        'correct_index': 3,
        'explanation': 'f-Strings beginnen mit dem Praefix f direkt vor dem Anfuehrungszeichen: f"text {var}".',
        'category': "Syntax",
        'difficulty': 1
    },
    {
        'question': "Was gibt `'Python'[0]` zurueck?",
        'options': ["y", "n", "P", "Error"],
        'correct_index': 2,
        'explanation': "String-Indizierung beginnt bei 0. Index 0 ist der erste Buchstabe 'P'.",
        'category': "Syntax",
        'difficulty': 2
    },
    {
        'question': "Was ist eine Type Hint in Python?",
        'options': [
            "Ein Befehl, der den Typ erzwingt",
            "Ein Kommentar ueber den erwarteten Typ",
            "Eine Typannotation, die dem Entwickler und der IDE hilft",
            "Ein Laufzeitfehler bei falschem Typ"
        ],
        'correct_index': 2,
        'explanation': "Type Hints sind optionale Annotationen. Python erzwingt sie nicht, aber IDEs und Tools (z.B. mypy) nutzen sie zur Fehlerentdeckung.",
        'category': "Syntax",
        'difficulty': 3
    },

    # ─── Exceptions ──────────────────────────────────────────────────────────────
    {
        'question': "Welche Exception wird bei `1 / 0` ausgeloest?",
        'options': ["ValueError", "TypeError", "ArithmeticError", "ZeroDivisionError"],
        'correct_index': 3,
        'explanation': "Division durch Null loest ZeroDivisionError aus.",
        'category': "Exceptions",
        'difficulty': 1
    },
    {
        'question': "Was ist der Typ des Fehlers bei `int('abc')`?",
        'options': ["TypeError", "SyntaxError", "ValueError", "NameError"],
        'correct_index': 2,
        'explanation': "'abc' kann nicht in int konvertiert werden → ValueError.",
        'category': "Exceptions",
        'difficulty': 2
    },
    {
        'question': "Was passiert, wenn eine Exception nicht abgefangen wird?",
        'options': [
            "Das Programm ignoriert den Fehler",
            "Python gibt eine Warnung aus",
            "Das Programm beendet sich und zeigt einen Traceback",
            "Der Rueckgabewert wird zu None"
        ],
        'correct_index': 2,
        'explanation': "Nicht abgefangene Exceptions beenden das Programm und zeigen einen Fehler-Traceback.",
        'category': "Exceptions",
        'difficulty': 2
    },
    # ─── Zusatzfragen ────────────────────────────────────────────────────────────
    {
        'question': "Was ist der Rueckgabetyp von `input()`?",
        'options': ["int", "bool", "str", "list"],
        'correct_index': 2,
        'explanation': "input() gibt immer einen String (str) zurueck, auch wenn der Nutzer eine Zahl eingibt.",
        'category': "Datentypen",
        'difficulty': 1
    },
    {
        'question': "Was ergibt `5 == 5.0` in Python?",
        'options': ["False", "TypeError", "None", "True"],
        'correct_index': 3,
        'explanation': "Python vergleicht Werte typuebergreifend: 5 (int) und 5.0 (float) sind wertgleich.",
        'category': "Operatoren",
        'difficulty': 2
    },
    {
        'question': "Wie oft wird der Schleifenkoerper ausgefuehrt?\n  i = 0\n  while i < 3:\n      i += 1",
        'options': ["2", "4", "3", "Endlosschleife"],
        'correct_index': 2,
        'explanation': "i startet bei 0 und wird bei 0, 1, 2 ausgefuehrt (jeweils < 3). Bei i=3 bricht die Schleife ab: 3 Durchlaeufe.",
        'category': "Kontrollstrukturen",
        'difficulty': 2
    },
]
