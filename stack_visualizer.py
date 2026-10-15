
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def make_table(step, item):
    table = Table(title=f"Parsing Step {step}", show_lines=True)
    table.add_column("Operator Stack", style="cyan")
    table.add_column("Operand / Tree Stack", style="green")
    table.add_column("Remaining Input", style="yellow")
    table.add_column("Action", style="magenta")

    table.add_row(
        item.get("operator_stack", item["stack"]),
        item.get("operand_stack", "—"),
        item["input"],
        item["action"],
    )

    return table


def show_trace(trace):
    table = Table(title="ParseVision - Parsing Trace", show_lines=True)
    table.add_column("Step", justify="right", style="cyan")
    table.add_column("Operator Stack", style="cyan")
    table.add_column("Operand / Tree Stack", style="green")
    table.add_column("Remaining Input", style="yellow")
    table.add_column("Action", style="magenta")

    for step, item in enumerate(trace):
        table.add_row(
            str(step),
            item.get("operator_stack", item["stack"]),
            item.get("operand_stack", "—"),
            item["input"],
            item["action"],
        )

    console.print(table)


def show_trace_step_by_step(trace):
    console.print(
        Panel(
            "[bold cyan]Step-by-Step Parsing[/bold cyan]\n"
            "Press Enter to advance to the next operation.",
            border_style="blue",
        )
    )

    for step, item in enumerate(trace):
        console.print(make_table(step, item))

        if step < len(trace) - 1:
            input("Press Enter for the next step...")
