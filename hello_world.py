import typer 
from typing import Optional

def main(a: str, b: int, c: Optional[float] = 3.14):
    typer.echo(f"Welcome to typer!")
    typer.echo(f"The value of <a> is {a}, the value of <b> is {b}")
    typer.echo(f"The value of <c> is {c}")

if __name__ == '__main__':
    typer.run(main)