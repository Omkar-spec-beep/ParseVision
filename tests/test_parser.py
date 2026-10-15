
import unittest

from lexer import tokenize
from parser import parse


class ParserTests(unittest.TestCase):

    def test_addition(self):
        root, _ = parse(tokenize("a + b"))
        self.assertEqual(root.value, "+")

    def test_operator_precedence(self):
        root, _ = parse(tokenize("a + b * c"))

        self.assertEqual(root.value, "+")
        self.assertEqual(root.children[0].value, "a")
        self.assertEqual(root.children[1].value, "*")

    def test_parentheses(self):
        root, _ = parse(tokenize("(a + b) * c"))

        self.assertEqual(root.value, "*")
        self.assertEqual(root.children[0].value, "+")

    def test_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            parse(tokenize("a + * b"))

    def test_missing_operand(self):
        with self.assertRaises(SyntaxError):
            parse(tokenize("a +"))


if __name__ == "__main__":
    unittest.main()
