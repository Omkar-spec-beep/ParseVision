
from rich.console import Console
from rich.panel import Panel

from lexer import tokenize
from parser import parse
from grammar import display_grammar
from stack_visualizer import show_trace, show_trace_step_by_step
from tree_visualizer import show_parse_tree

console = Console()


def main():
    while True:
        console.print(
            Panel(
                "[bold cyan]PARSEVISION[/bold cyan]\n"
                "Interactive Compiler Design Project\n\n"
                "[1] Parse an expression (full trace)\n"
                "[2] Parse step by step\n"
                "[3] View grammar rules\n"
                "[0] Exit",
                title="Compiler Design Visualizer",
                border_style="blue",
            )
        )

        choice = input("Choose an option: ").strip()

        # Exit the application
        if choice == "0":
            console.print("[bold cyan]Goodbye![/bold cyan]")
            break

        # Display grammar rules
        if choice == "3":
            display_grammar()
            input("\nPress Enter to return to the menu...")
            continue

        # Validate menu selection
        if choice not in ("1", "2"):
            console.print("[red]Invalid option. Try again.[/red]")
            continue

        # Get the expression
        expression = input("\nEnter an expression: ").strip()

        try:
            # Tokenize and parse the expression
            tokens = tokenize(expression)
            root, trace = parse(tokens)

            console.print(
                "\n[bold green]Parsing successful![/bold green]"
            )

            # Display the parsing trace
            if choice == "1":
                show_trace(trace)
            else:
                show_trace_step_by_step(trace)

            # Display the final parse tree
            show_parse_tree(root)

        except (ValueError, SyntaxError) as error:
            console.print(
                f"\n[bold red]Parsing failed:[/bold red] {error}"
            )

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
