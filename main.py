import typer

from prr.commands.generate import app as generate
from prr.commands.init import app as initialize_pr

app = typer.Typer()
app.add_typer(generate, name="generate")
app.add_typer(initialize_pr, name="init")

if __name__ == "__main__":
    try:
        app()
    except Exception as e:
        print(f"Error: {e}")
