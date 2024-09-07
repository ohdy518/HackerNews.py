# import rich
from rich.console import Console
from rich.table import Table
import fetcher

console = Console()

def header():
    console.rule("[bold orange1]Hacker News[/]", style="bold orange3")

def top():
    table = Table(title="top stories", title_style="bold orange1")
    table.add_column("[bold italic yellow3]SEL[/]", style="bold italic yellow3")
    table.add_column("[orange3]score[/]", style="orange3")
    table.add_column("[bold orange1]title[/]", style="bold orange1")
    table.add_column("[orange3]url[/]", style="orange3")
    table.add_column("[orange3]by[/]", style="orange3")

    console.print("[italic yellow]fetching top stories...[/]", style="italic yellow", end="\r")
    results = fetcher.top()
    console.print(" "*30, end="\n")
    console.clear()
    header()

    selector_number = 0

    for i in results:
        table.add_row(
            str(selector_number),
            str(i["score"]),
            i["title"],
            str(i["url"])[8:30]+"...",
            str(i["by"]) if len(str(i["by"])) <= 12 else str(i["by"])[:12]+"..."
        )
        selector_number += 1

    console.print(table)

def sel(selector):
    selector = int(selector)
    console.print("[italic yellow]fetching...[/]", style="italic yellow", end="\n")
    result = fetcher.sel(selector)
    console.clear()
    header()
    console.print(f"\[BASIC INFO]\ntitle: [bold orange1]{result["title"]}[/]\n  url: {result['url']}\n   by: {result['by']}", style="orange3")
    console.line()
    console.print(f"\[CONTENT]\n[bold orange1]{result["text"] if "text" in result else "(empty)"}[/]", style="orange3")

def fetch_progress(now, total):
    console.print(" "*30, end="\r")
    console.print(f"[italic yellow]fetching {now}/{total}...[/]", style="italic yellow", end="\r")