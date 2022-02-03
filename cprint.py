import typer

def main(name: str):
    string_style = typer.style(name, fg=typer.colors.RED, bold = True)
    message = f"Welcome "
    typer.echo(message + string_style)
    typer.secho(f"The other way {name}",fg=typer.colors.RED)
    typer.echo(f"This goes to standard error!", err=True)
if __name__ == '__main__':
    typer.run(main)