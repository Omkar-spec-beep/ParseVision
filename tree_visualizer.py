
from tree import print_tree


def show_parse_tree(root):
    """Display the final parse tree."""

    print("\n" + "=" * 40)
    print("          PARSE TREE")
    print("=" * 40)

    print_tree(root)

    print("=" * 40)
