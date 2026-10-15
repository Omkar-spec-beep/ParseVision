
import re


TOKEN_PATTERN = re.compile(
    r"\s*(?:(\d+(?:\.\d+)?)|([A-Za-z_]\w*)|(.))"
)


def tokenize(expression):
    """Convert an expression into a list of tokens."""

    tokens = []

    for match in TOKEN_PATTERN.finditer(expression):
        number, identifier, symbol = match.groups()

        if number:
            tokens.append(number)

        elif identifier:
            tokens.append(identifier)

        elif symbol in {"+", "-", "*", "/", "(", ")"}:
            tokens.append(symbol)

        else:
            raise ValueError(
                f"Invalid character: {symbol!r}"
            )

    if not tokens:
        raise ValueError("Expression cannot be empty.")

    return tokens
