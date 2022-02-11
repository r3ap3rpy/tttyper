import typer
import click

@click.group()
def cli():
    ...

@cli.command()
def init():
    click.echo("Initializing!")

@cli.command()
def drop():
    click.echo("Dropping!")

app = typer.Typer()

@app.command()
def sub():
    typer.echo("Typer is now included in the Click main app!")

typer_click_object = typer.main.get_command(app)
cli.add_command(typer_click_object, "sub")

if __name__ == '__main__':
    cli()