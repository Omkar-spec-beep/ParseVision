
from tree import Node

PRECEDENCE = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def parse(tokens):
    """Parse arithmetic expressions and record every operation."""

    values = []
    operators = []
    remaining = list(tokens)
    trace = []
    expect_operand = True

    def display_stack():
        parts = []

        for index, operator in enumerate(operators):
            parts.append(operator)

            if index < len(values):
                parts.append(str(values[index].value))

        if len(values) > len(operators):
            parts.append(str(values[-1].value))

        return "$ " + " ".join(parts)

    # def record(action):
    #     trace.append({
    #         "stack": display_stack(),
    #         "input": " ".join(remaining) + " $",
    #         "action": action,
    #     })
    
    def record(action):
        trace.append({
            "stack": display_stack(),
            "operator_stack": " ".join(operators) if operators else "$",
            "operand_stack": " ".join(str(value.value) for value in values) if values else "—",
            "input": " ".join(remaining) + " $",
            "action": action,
        })


    def reduce_once():
        if not operators or operators[-1] not in PRECEDENCE:
            raise SyntaxError("Invalid operator")

        if len(values) < 2:
            raise SyntaxError("Operator is missing an operand")

        operator = operators.pop()
        right = values.pop()
        left = values.pop()

        values.append(Node(operator, [left, right]))
        record(f"REDUCE E -> E {operator} E")

    record("START")

    for token in tokens:

        # Identifier or number
        if token not in PRECEDENCE and token not in ("(", ")"):
            if not expect_operand:
                raise SyntaxError(f"Unexpected operand: {token}")

            values.append(Node(token))
            remaining.pop(0)
            expect_operand = False
            record(f"SHIFT {token}")

        # Opening parenthesis
        elif token == "(":
            if not expect_operand:
                raise SyntaxError("Missing operator before '('")

            operators.append("(")
            remaining.pop(0)
            expect_operand = True
            record("SHIFT (")

        # Closing parenthesis
        elif token == ")":
            if expect_operand:
                raise SyntaxError("Missing operand before ')'")

            while operators and operators[-1] != "(":
                reduce_once()

            if not operators:
                raise SyntaxError("Unmatched closing parenthesis")

            operators.pop()
            remaining.pop(0)
            expect_operand = False
            record("MATCH PARENTHESES")

        # Arithmetic operator
        else:
            if expect_operand:
                raise SyntaxError(
                    f"Operator {token!r} has no left operand"
                )

            while (
                operators
                and operators[-1] != "("
                and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]
            ):
                reduce_once()

            operators.append(token)
            remaining.pop(0)
            expect_operand = True
            record(f"SHIFT {token}")

    if expect_operand:
        raise SyntaxError("Expression ends with a missing operand")

    while operators:
        if operators[-1] == "(":
            raise SyntaxError("Unmatched opening parenthesis")
        reduce_once()

    if len(values) != 1:
        raise SyntaxError("Invalid expression")

    record("ACCEPT")
    return values[0], trace
