
# class Node:
#     """Represents a node in the parse tree."""

#     def __init__(self, value, children=None):
#         self.value = str(value)
#         self.children = children if children is not None else []

class Node:
    """Represents a node in the parse tree."""

    def __init__(self, value, children=None):
        self.value = value.value if isinstance(value, Node) else str(value)
        self.children = children if children is not None else []



def print_tree(node, prefix="", is_last=True, is_root=True):
    """Print the parse tree using ASCII branches."""

    if not isinstance(node, Node):
        print(prefix + str(node))
        return

    if is_root:
        print(node.value)
    else:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + node.value)

    child_prefix = prefix if is_root else (
        prefix + ("    " if is_last else "│   ")
    )

    for index, child in enumerate(node.children):
        print_tree(
            child,
            prefix=child_prefix,
            is_last=(index == len(node.children) - 1),
            is_root=False,
        )
