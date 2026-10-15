
GRAMMAR = {
    "E": [
        ["E", "+", "T"],
        ["E", "-", "T"],
        ["T"],
    ],
    "T": [
        ["T", "*", "F"],
        ["T", "/", "F"],
        ["F"],
    ],
    "F": [
        ["(", "E", ")"],
        ["id"],
        ["num"],
    ],
}


def display_grammar():
    """Print the grammar rules."""
    print("\n" + "=" * 45)
    print("           PARSEVISION GRAMMAR")
    print("=" * 45)

    for non_terminal, productions in GRAMMAR.items():
        alternatives = [" ".join(rule) for rule in productions]
        print(f"{non_terminal} -> {' | '.join(alternatives)}")

    print("=" * 45)
